"""Fixed-horizon randomized holdout study, with ITT and sample-ratio checks."""
import math
import random
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from common import database, export_query, report, table, write_csv

ROOT=Path(__file__).resolve().parent


def estimate(n_t,y_t,n_c,y_c,spend):
    if min(n_t,n_c)<=0 or not (0<=y_t<=n_t and 0<=y_c<=n_c) or spend<0:
        raise ValueError('Invalid experiment counts or spend')
    pt,pc=y_t/n_t,y_c/n_c
    delta=pt-pc
    se=math.sqrt(pt*(1-pt)/n_t+pc*(1-pc)/n_c)
    pooled=(y_t+y_c)/(n_t+n_c)
    null_se=math.sqrt(pooled*(1-pooled)*(1/n_t+1/n_c))
    p=math.erfc(abs(delta/null_se)/math.sqrt(2)) if null_se else (1 if delta==0 else 0)
    lo,hi=delta-1.96*se,delta+1.96*se
    incremental=n_t*delta
    expected=(n_t+n_c)/2
    chi2=((n_t-expected)**2+(n_c-expected)**2)/expected
    return dict(absolute_lift=delta,relative_lift=delta/pc if pc else None,
                ci95_lower=lo,ci95_upper=hi,p_value=p,incremental_members=incremental,
                incremental_cac_usd=spend/incremental if incremental>0 else None,
                icac_ci_lower_usd=spend/(n_t*hi) if hi>0 else None,
                icac_ci_upper_usd=spend/(n_t*lo) if lo>0 else None,
                srm_p_value=math.erfc(math.sqrt(chi2/2)))


def main():
    rng=random.Random(52)
    rows=[]
    for i in range(40000):
        treatment=rng.random()<.5
        exposed=treatment and rng.random()<.8
        converted=int(rng.random()<(.055 if exposed else .04))
        rows.append(dict(user_id=f'sim-{i:05}',arm='Treatment' if treatment else 'Control',
                         exposed=int(exposed),converted=converted,net_revenue_usd=round(converted*136.8,2)))
    write_csv(ROOT/'data/experiment_users.csv',rows)
    db=database(ROOT/'outputs/analysis.sqlite',{'experiment_users':rows})
    arms=export_query(db,ROOT/'analysis.sql',ROOT/'outputs/arm_summary.csv')
    c,t=arms
    stats=estimate(t['assigned_users'],t['conversions'],c['assigned_users'],c['conversions'],12000)
    write_csv(ROOT/'outputs/lift_estimates.csv',[stats])
    # Approximate fixed sample size, two-sided alpha .05, 80% power.
    p0=.04; mde=.01; p1=p0+mde; pbar=(p0+p1)/2
    n=math.ceil(((1.96*math.sqrt(2*pbar*(1-pbar))+.8416*math.sqrt(p0*(1-p0)+p1*(1-p1)))**2)/(mde*mde))
    decision='Advance to a limited replication test' if stats['ci95_lower']>0 and stats['srm_p_value']>=.01 else 'Do not scale; investigate validity or gather the preplanned sample'
    report(ROOT,'Paid Social Incrementality & Lift',{'Absolute lift':f"{stats['absolute_lift']*100:.2f} pp",'95% lift interval':f"{stats['ci95_lower']*100:.2f}–{stats['ci95_upper']*100:.2f} pp",'Incremental members':f"{stats['incremental_members']:.1f}",'Incremental CAC':f"${stats['incremental_cac_usd']:.2f}"},
           [table('Randomized arms',arms,'arm','conversion_rate'),table('Lift and validity estimates',[dict(study='Paid social holdout',**stats)],'study','absolute_lift')],
           [f"{decision}. Treatment versus control is evaluated by original assignment, including unexposed treatment users.",
            f"The estimated {stats['relative_lift']:.1%} relative lift has a two-sided p-value of {stats['p_value']:.3g}; sample-ratio mismatch p={stats['srm_p_value']:.3f}.",
            f"A planning baseline of 4% and a 1 percentage-point minimum detectable effect requires approximately {n:,} users per arm at 80% power. This simulated study has about 20,000 per arm.",
            'Recommend that the analyst, media buyer, and measurement partner agree on holdout exclusions and a fixed decision date before launch. This is a proposed collaboration workflow.'],
           'Synthetic user-level randomized study of a single campaign. $12,000 is the assumed incremental treatment media cost; control media cost is zero. Normal-approximation confidence intervals are appropriate to these large counts, not rare-event samples. No peeking, cross-user spillover, or identity errors are simulated. iCAC interval is derived by inverting the lift interval and is undefined/unbounded when lift includes zero. This demonstrates a platform-lift analysis without claiming execution of a real platform study.')
    db.close()


if __name__=='__main__': main()

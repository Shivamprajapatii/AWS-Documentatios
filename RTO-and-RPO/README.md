# 🔥 What Is Disaster Recovery (DR)?
    If something bad happens (like a data center goes down, a cyberattack, or accidental data deletion), DR is how you bounce back — quickly, safely, and without major data loss.

# ⚙️ What Is High Availability (HA)?
    High Availability (HA) is about keeping your systems running — all the time, with minimal downtime, even if something breaks.

# 🚨 Common Disaster Scenarios:
- App Level - Bugs, crashes, config errors.
- User Level - Accidental deletion, bad deployment.
- Infra Level - Hardware failure, disk crash.
- Network Level - DNS failure, DDoS attack.
- Cloud Provider Level - AWS region outage, AZ failure.
- Natural Level - Earthquake, fire in data center.


# 🧍‍♂️ Who Is Responsible?
- App bugs / configs - Developer or DevOps team
- Data loss (user error) - DBA, backup strategy
- Server failure - AWS (hardware), but you're responsible for resilience
- Regional outage - You (architect system for DR across regions)
- Cyberattack - You (implement IAM, WAF, security best practices)

# 🏗️ In AWS Terms:
- High Availability - Multi-AZ deployments, Load Balancers, Auto Scaling
- Disaster Recovery - S3 CRR, DRS, Route 53 Failover, Aurora Global DB

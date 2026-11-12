
# MONITORING DEPLOYED SYSTEMS

## The need for monitoring 

- to detect failures faster than end users
- faster diagnosis of the problem
- to anticipate capacity problems
- drive business and cost decisions

## worst--best case preparation

| Position   | Protecting Against                    | Monitoring's role                                 | Typical signal                                 |
| ---------- | ------------------------------------------------- | ------------------------------------------------- | ---------------------------------------------- |
| Worst case | Outage, data loss, dependency failure, breach     | Detect fast, bound blast radius, trigger rollback | Error rate, availability, failed health checks |
| Base case  | Slow drift, creeping latency, capacity exhaustion | Trend and forecast, stay within SLO               | Saturation, p95 latency, error budget burn     |
| Best case  | Demand spike you can't serve, wasted headroom     | Prove headroom, tune cost, show reliability       | Traffic rate, throughput per pound, adoption   |

Worst case monitoring looks at 3 things:

- it tells you you're in the worst case
- it tells you how far the damage has spread
- gives you the trigger for the contingency plan you already wrote

Base case is the everyday swing range between worst and best, main job is to keep the system
in the good end of the range.

Best case scenarios assume favourable conditions such as 

- higher demand
- better conversion
- everything lands on schedule
- faster-than-expected adoption or uptake
- costs come in under budget
- dependencies and integrations deliver without rework
- churn or error rates stay below forecast
- hiring and training fill faster than planned

```mermaid
flowchart LR
    subgraph S1["1 · WORST"]
        direction TB
        A1["App VM"] --> B1["CPU load monitored<br/>by cloud service"] --> C1["Not used"] --> D1["Falls over!"]
    end
    subgraph S2["2"]
        direction TB
        A2["App VM"] --> B2["CPU load monitored<br/>by cloud service"] --> C2["Dashboard"] --> D2["Miss it?"]
    end
    subgraph S3["3"]
        direction TB
        A3["App VM"] --> B3["CPU load monitored<br/>by cloud service"] --> C3["Alarm"] --> D3["Notification"]
    end
    subgraph S4["4 · BEST"]
        direction TB
        A4["App VM"] --> B4["CPU load monitored<br/>by cloud service"] --> C4["<b>Auto scaling</b><br/>AWS EC2 Auto Scaling<br/>Azure VM Scale Sets<br/>GCP Instance Group"]
    end
    

    S1 ~~~ S2 ~~~ S3 ~~~ S4 

    classDef vm fill:#F59E0B,stroke:#7C4A03,stroke-width:2px,color:#000,font-weight:bold
    classDef cpu fill:#475569,stroke:#1E293B,stroke-width:2px,color:#fff
    classDef step fill:#1E3A8A,stroke:#0F1E4A,stroke-width:2px,color:#fff,font-weight:bold
    classDef bad fill:#DC2626,stroke:#7F1D1D,stroke-width:2px,color:#fff,font-weight:bold
    classDef meh fill:#EA580C,stroke:#7C2D12,stroke-width:2px,color:#fff,font-weight:bold
    classDef good fill:#059669,stroke:#064E3B,stroke-width:2px,color:#fff,font-weight:bold
    classDef best fill:#7C3AED,stroke:#3B0764,stroke-width:2px,color:#fff
    class A1,A2,A3,A4 vm
    class B1,B2,B3,B4,M1,M2,M3 cpu
    class C1,C2,C3 step
    class D1 bad
    class D2 meh
    class D3 good
    class C4 best

    style S1 fill:#FEE2E2,stroke:#DC2626,stroke-width:2px,color:#000
    style S2 fill:#FFEDD5,stroke:#EA580C,stroke-width:2px,color:#000
    style S3 fill:#D1FAE5,stroke:#059669,stroke-width:2px,color:#000
    style S4 fill:#EDE9FE,stroke:#7C3AED,stroke-width:2px,color:#000
  
    linkStyle 0,1,2,3,4,5,6,7,8,9,10 stroke:#111,stroke-width:2px
```


## Performance testing -- Documentation

1. Launch app instance and SSH in, check if the browser works
2. go to instance summary, click monitoring in tags

![Screenshot 2026-10-28 at 15.37.51.png](images/Screenshot%202026-10-28%20at%2015.37.51.png)

3. Click manged detailed monitoring - [ X ] tick enabled
4. Click confirm, then click the 3 dots on the right side, then add dashboard
5. Click on add dashboard > create dashboard >add new

![Screenshot 2026-10-28 at 15.43.49.png](images/Screenshot%202026-10-28%20at%2015.43.49.png)

# using apache package to simulate network traffic

6. Go to the VM root


```bash
sudo apt install apache2-utils
 ab -n 1000 -c 10 http://18.203.156.41/  # ip address of the app
```

apache bench is used for this (ab) command

- this should produce noticeable spikes in the dashboard

# Alarm alert for cpu usage - with email notification

1. Find instance ID
2. EC2 → Instances → tick the instance → Actions → Monitor and troubleshoot → Manage CloudWatch alarms.
3. Set up email Notification → Alarm state trigger: In alarm
4. Send a notification to: Create new topic
- Topic name: tech613-daria-cpu-alarm
- Email endpoints: <your-name>@email.com
5. click create topic then click next
6. Confirm the email via email (from aws)
7. Add the alarm to the dashboard - CloudWatch → Alarms → tick the alarm → Actions → Add to dashboard → choose the app dashboard.

dashboard 
![Screenshot 2026-10-28 at 16.54.13.png](images/Screenshot%202026-10-28%20at%2016.54.13.png)
Email
![Screenshot 2026-10-28 at 16.52.42.png](images/Screenshot%202026-10-28%20at%2016.52.42.png)

![Screenshot 2026-10-28 at 16.43.48.png](images/Screenshot%202026-10-28%20at%2016.43.48.png)

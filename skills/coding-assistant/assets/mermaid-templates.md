# Architecture Templates

Use these Mermaid templates to quickly visualize system designs.

## Layered Architecture (Standard)

```mermaid
graph TB
    subgraph Presentation
        API[API Controller]
        Web[Web Controller]
    end

    subgraph Business["Business Layer"]
        Service[Service Class]
        Validator[Validator]
    end

    subgraph Data["Data Access Layer"]
        Repo[Repository]
        Model[Eloquent Model]
    end

    subgraph Infra["Infrastructure"]
        DB[(Database)]
        Cache[(Redis)]
        Queue[Message Queue]
    end

    API --> Service
    Web --> Service
    Service --> Validator
    Service --> Repo
    Repo --> Model
    Model --> DB
    Repo -.-> Cache
```

## Hexagonal Architecture (Ports & Adapters)

```mermaid
graph TB
    subgraph Core["Domain Core"]
        Entity[Domain Entity]
        UseCase[Use Case / Service]
        PortIn[Input Port (Interface)]
        PortOut[Output Port (Interface)]
    end

    subgraph AdaptersIn["Primary Adapters"]
        Web[Web Controller]
        CLI[Console Command]
    end

    subgraph AdaptersOut["Secondary Adapters"]
        DBAdapter[Persistence Adapter]
        EmailAdapter[Email Adapter]
    end

    Web --> PortIn
    CLI --> PortIn
    PortIn -.-> UseCase
    UseCase --> Entity
    UseCase --> PortOut
    DBAdapter -.-> PortOut
    EmailAdapter -.-> PortOut
```

## Event-Driven Architecture

```mermaid
graph LR
    subgraph Producer
        ServiceA[Order Service]
        EventA[OrderCreated Event]
    end

    subgraph Broker
        Exchange((Exchange))
        Queue1[Inventory Queue]
        Queue2[Notification Queue]
    end

    subgraph Consumers
        ServiceB[Inventory Service]
        ServiceC[Notification Service]
    end

    ServiceA --> EventA
    EventA --> Exchange
    Exchange --> Queue1
    Exchange --> Queue2
    Queue1 --> ServiceB
    Queue2 --> ServiceC
```

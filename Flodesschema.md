# Flödesschema för systemövervakning

```mermaid
graph TD
    %% Startpunkt
    A["Användare (interagerar med programmet)"]

    %% Externa Resurser
    subgraph "Externa Resurser"
        F[Operativsystem / psutil]
    end

    %% Huvudflöde
    subgraph "Programmets Kärna"
        direction TB
        B(menu.py)
        C(main.py)
    end

    %% Funktionsmoduler med tråd
    subgraph "Funktionsmoduler"
        direction LR
        E[alarms.py]
        subgraph M["monitoring.py"]
            D["Huvudfunktion"]
            D_thread["Bakgrundstråd för live-övervakning"]
        end
    end

    %% ---- Flöden ----
    A --> |"Väljer menyval"| B
    B --> |"Returnerar val"| C
    C --> |"Anropar skapa/visa larm"| E
    C --> |"Anropar start/visa status eller live-övervakning"| D
    D --> |"Startar bakgrundstråd"| D_thread
    D --> |"Hämtar CPU, minne, disk"| F
    D_thread --> |"Live-övervakning loop"| A
    E --> |"Visar konfigurerade larm"| A
    E -.-> |Levererar 'alarms_list'| D
    D --> |"Visar status / VARNING!"| A

    %% ---- Styling ----
    classDef main_core fill:#bbf,stroke:#333,stroke-width:2px;
    class C main_core;
    classDef user_int fill:#cfc,stroke:#333;
    class A user_int;
    classDef module fill:#ccf,stroke:#333;
    class D,E,D_thread module;
    classDef external fill:#eee,stroke:#333;
    class F external;

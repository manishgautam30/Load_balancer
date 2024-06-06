# Load Balancer

## Milestone 1: Design and Functionality

### Setup Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/manishgautam30/load_balancer.git
    cd load_balancer
    ```

2. **Set up a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the mock API server**:
    ```bash
    python src/mock_apis.py
    ```

5. **Run the main script**:
    ```bash
    python src/main.py
    ```

## Design Choices

- **Dynamic Routing**:
    - Based on API type, request payload size, and randomized routing.
- **Mock API Endpoints**:
    - Simulated fast and slow responses using Flask.
- **Logging**:
    - Captured request details, endpoint selection, and response times in `load_balancer.log`.

## Usage Instructions

- Run the mock API server to simulate different API responses.
- Run the main script to simulate requests and test the load balancer.
- Check the `load_balancer.log` file for detailed logs.

## Milestone 2: Queue Management and Analysis

### Performance Analysis

#### FIFO Queue

- FIFO (First-In-First-Out) processes requests in the order they arrive.
- Pros: Simple and predictable.
- Cons: May lead to long wait times for high-priority requests.

#### Priority Queue

- Processes requests based on their priority.
- Pros: High-priority requests are handled first.
- Cons: Lower-priority requests may experience delays.

#### Round Robin Queue

- Distributes requests evenly across multiple queues.
- Pros: Balances load evenly.
- Cons: May not prioritize urgent requests effectively.

### Analysis

- **FIFO**: All requests were processed in the order they arrived. Suitable for environments where request order is critical.
- **Priority**: High-priority requests were processed faster. Ideal for scenarios with varying request importance.
- **Round Robin**: Requests were evenly distributed, reducing the risk of any single endpoint being overloaded. Effective for balancing load but may not be suitable for varying priority levels.

## Link to Hosted application
https://tarun-tailor-wasserstoff-backend-task.vercel.app/


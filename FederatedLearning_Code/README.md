# Federated Learning — Experiments & Code

Federated Learning (FL) trains a shared model without requiring the movement of raw data. Each client trains locally, sends **model updates** (not data) to a server, and the server aggregates them. This preserves privacy and reduces central data transfer while still producing a global model.

---

## What’s in here

- **Simulation with Flower**: FL experiments using the Flower framework (local clients simulated on one machine).
- **Algorithms**: **FedAvg** and **FedProx** 
- **Baselines**: Centralized (single dataset) training for comparison.
- **Eval**: A **global test set** for comparison across centralized vs FL runs (accuracy, precision/recall/F1, confusion matrix).
- **Use cases**:
  - *Industrial manufacturing* defect classification (private; **not included**).
  - *Public benchmark* dataset (**included for reference**) so you can run the pipeline.

 **Data note**: Due to privacy/IP constraints, the real manufacturing dataset is not shared. The repo contains a **public benchmark** to demonstrate the full code path. To reproduce a similar setup, place your data locally.

## How to run

```bash
# from the repo root
cd FederatedLearning_Code

# 1) Create & activate a virtual env
python -m venv .venv
# Windows (PowerShell):
. .\.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

# 2) Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 3) Run centralized baseline (benchmark data)
python -m src.train_centralized --dataset benchmark --epochs 10 --batch-size 32 --lr 1e-3

# 4) Run FL — FedAvg (N clients, R rounds)
python -m src.simulate_fedavg --dataset benchmark --clients 3 --rounds 5 --local-epochs 5 --batch-size 32 --lr 1e-3

# 5) Run FL — FedProx (add proximal strength mu)
python -m src.simulate_fedprox --dataset benchmark --clients 3 --rounds 5 --local-epochs 5 --batch-size 32 --lr 1e-3 --mu 0.01

# 6) Outputs
# Metrics, curves, and confusion matrices 

requirements.txt
flwr
torch
torchvision
numpy
pandas
scikit-learn
matplotlib
seaborn
tqdm
ipykernel
jupyter


import torch

if torch.cuda.is_available():
    print("CUDA is available")
    print(f"PyTorch version: {torch.__version__}")
    print(f"CUDA version: {torch.version.cuda}")
else:
    print("CUDA is not available")

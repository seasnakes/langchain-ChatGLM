import torch.cuda
import torch.backends

def torch_gc(DEVICE):
    if torch.cuda.is_available():
        with torch.cuda.device(DEVICE):
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
    elif torch.backends.mps.is_available():
        try:
            import torch.mps
            torch.mps.empty_cache()
        except Exception as e:
            print(e)
            print("如果您使用的是 macOS 建议将 pytorch 版本升级至 2.0.0 或更高版本，以支持及时清理 torch 产生的内存占用。")
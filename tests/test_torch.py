import torch


def test_rocm_available():
    assert torch.cuda.is_available(), "ROCm not available"


def test_tensor_on_gpu():
    x = torch.tensor([1.0, 2.0, 3.0]).cuda()
    assert x.device.type == "cuda"
    assert x.sum().item() == 6.0

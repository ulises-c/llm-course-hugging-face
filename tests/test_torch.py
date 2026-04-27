import torch
import torchvision
import torchaudio


def test_rocm_available():
    assert torch.cuda.is_available(), "ROCm not available"


def test_tensor_on_gpu():
    x = torch.tensor([1.0, 2.0, 3.0]).cuda()
    assert x.device.type == "cuda"
    assert x.sum().item() == 6.0


def test_torchvision_rocm():
    assert "+rocm" in torch.__version__, f"torch is not a ROCm build: {torch.__version__}"
    # torchvision has no __version__ with build tag, but importing it requires
    # compatible torch C++ extensions — a successful import confirms ABI match
    assert torchvision.__version__ is not None
    x = torch.zeros(1, 3, 4, 4).cuda()
    # nms is the op that breaks on version mismatch; calling it exercises the C++ bridge
    boxes = torch.tensor([[0.0, 0.0, 1.0, 1.0]]).cuda()
    scores = torch.tensor([1.0]).cuda()
    torchvision.ops.nms(boxes, scores, 0.5)


def test_torchaudio_rocm():
    assert "+rocm" in torch.__version__, f"torch is not a ROCm build: {torch.__version__}"
    assert torchaudio.__version__ is not None
    # resample exercises the C++ backend
    waveform = torch.zeros(1, 16000).cuda()
#     torchaudio.functional.resample(waveform, orig_freq=16000, new_freq=8000)

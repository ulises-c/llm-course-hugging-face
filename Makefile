.PHONY: install kernel test

# torch is excluded from pyproject.toml because Poetry cannot resolve the
# +rocm7.2 local-version identifier alongside PyPI wheels.
install:
# 	poetry install --no-cache
	poetry run pip install --force-reinstall --no-deps \
	  --index-url https://download.pytorch.org/whl/rocm7.2 \
	  "torch==2.11.0+rocm7.2" \
	  "torchvision" \
	  "torchaudio"
	$(MAKE) kernel

kernel:
	poetry run python -m ipykernel install --user \
	  --name llm-course-hugging-face \
	  --display-name "HuggingFace LLM Course (ROCm)"

test:
	poetry run pytest -v
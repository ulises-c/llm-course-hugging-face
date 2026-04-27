.PHONY: install kernel

# torch is excluded from pyproject.toml because Poetry cannot resolve the
# +rocm6.3 local-version identifier alongside PyPI wheels.
install:
	poetry install
	poetry run pip install --force-reinstall --no-deps \
	  --index-url https://download.pytorch.org/whl/rocm6.3 \
	  "torch==2.9.1+rocm6.3"
	$(MAKE) kernel

kernel:
	poetry run python -m ipykernel install --user \
	  --name llm-course-hugging-face \
	  --display-name "HuggingFace LLM Course (ROCm)"

from huggingface_hub import snapshot_download
snapshot_download(
    repo_id="mistralai/Voxtral-Mini-3B-2507",
    local_dir="./models/mistralai/Voxtral-Mini-3B-2507",
    ignore_patterns=["*.safetensors"]  # Optionnel
)
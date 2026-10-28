from pathlib import Path
from datasets import load_dataset

print("Loading Samanantar English-Kannada dataset...")
ds = load_dataset("ai4bharat/samanantar", "kn", split="train", streaming=True)

output_dir = Path.cwd()
en_path = output_dir / "train.en"
kn_path = output_dir / "train.kn"

print("Extracting 10,000 sentence pairs...")
count = 0

with en_path.open("w", encoding="utf-8") as f_en, \
     kn_path.open("w", encoding="utf-8") as f_kn:
    for item in ds:
        src = item.get("src") or item.get("en") or item.get("source") or ""
        tgt = item.get("tgt") or item.get("kn") or item.get("target") or ""
        
        if isinstance(item.get("translation"), dict):
            src = item["translation"].get("en", src)
            tgt = item["translation"].get("kn", tgt)

        src = str(src).strip()
        tgt = str(tgt).strip()

        if src and tgt:
            f_en.write(src + "\n")
            f_kn.write(tgt + "\n")
            count += 1
            
            if count % 2000 == 0:
                print(f"Extracted {count} pairs...")
                
            if count >= 10000:
                break

print(f"Successfully generated {count} lines into train.en and train.kn!")
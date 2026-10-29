# M1 Moses English-to-Kannada Baseline

## Model
- System: Moses phrase-based machine translation
- Direction: English to Kannada
- Decoder: ~/mosesdecoder/bin/moses
- Configuration: results/m1/config/moses.ini

## Evaluation sets
- FLORES dev: 997 sentence pairs
- FLORES devtest: 1,012 sentence pairs
- IN22-Gen: 1,024 sentence pairs

All prediction/reference line counts matched.

## Results

| Dataset | BLEU | chrF++ | spBLEU-1K |
|---|---:|---:|---:|
| FLORES dev | 0.0 | 11.0 | 1.1 |
| FLORES devtest | 0.1 | 10.9 | 0.9 |
| IN22-Gen | 0.1 | 10.0 | 0.8 |

## Artifacts
- Predictions: results/m1/*.pred.kn
- BLEU/chrF++ metrics: results/m1/*.metrics.txt
- spBLEU metrics: results/m1/*.spbleu.txt
- Model configuration: results/m1/config/moses.ini
- Run metadata: results/m1/config/run-info.txt

## Conclusion
M1 is a verified English-to-Kannada phrase-based Moses baseline. These scores are the baseline for comparison with M2, M3, and M4.

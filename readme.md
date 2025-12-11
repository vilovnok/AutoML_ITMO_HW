# Sberbank Russian Housing Market

[Соревнование](https://www.kaggle.com/competitions/sberbank-russian-housing-market/overview)

## Задача
Предсказание цены драгоценных камней на основе табличных данных.
Метрика: RMSLE (Root Mean Squared Logarithmic Error)
$$
\text{RMSLE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left( \log(1 + \hat{y}_i) - \log(1 + y_i) \right)^2 }
$$




## Результаты


Лучшее решение ...


## Структура проекта
```
├── data/
│   ├── raw/                            # train.csv, test.csv, macro.csv
│   └── processed/                      
├── pybook/
│   ├── eda.ipynb                    # EDA
│   ├── 02_lama_baseline.ipynb          # LAMA baseline
│   ├── 03_custom_solution.ipynb        # Custom solution
│   └── 04_test_pipeline.ipynb          # Тест pipeline
├── src/
│   ├── __init__.py
│   └── pipeline.py                     # GemstoneEnsemble 
└── pyproject.toml                      # Конфигурация 
```
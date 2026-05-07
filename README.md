# Customer support agent
> MLE case for bynder

## Running
chainlit run app.py

## Logging
Set log level with `LOG_LEVEL`:

```bash
LOG_LEVEL=DEBUG chainlit run app.py
```

Valid levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.

## Improvements
- tool to allow model to query the info itself if needed
- multi modal ? screenshot of the issue
- model switching based on similarity from query and retrieved from rag (similar = easy = dumb model, not similar = hard = smart model)
- imporove the citing logic, weak letting to the model decide

- tradeoff of more tokens vs more calls

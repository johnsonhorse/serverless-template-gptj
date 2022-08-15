import banana_dev as banana
import os

api_key = os.environ.get("API_KEY")
model_key = os.environ.get("MODEL_KEY")

#model_inputs = {'prompt': 'My favorite part about working with AI is'}
model_inputs = {'prompt': 'The best part about learning is', 'max_length':300, 'do_sample':True}

model_outputs = banana.run(api_key, model_key, model_inputs)

print(model_outputs)
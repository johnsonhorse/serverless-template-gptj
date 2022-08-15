# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``

import requests
import json

model_inputs = {'prompt': 'My favorite part about working with AI is', 'max_length':500, 'do_sample':True}


res = requests.post('http://localhost:8000/', json = model_inputs)
res_dict = json.loads(res.text)
print(res_dict['output'])
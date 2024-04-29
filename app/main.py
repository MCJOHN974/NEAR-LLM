from transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_model(model_path):
    model = GPT2LMHeadModel.from_pretrained(model_path)
    tokenizer = GPT2Tokenizer.from_pretrained(model_path)
    return model, tokenizer

def generate_text(prompt, model, tokenizer):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Load the model from the final checkpoint
model, tokenizer = load_model('./results/final_model')

# Generate text

prompt = input("Prompt> ")
generated_text = generate_text(prompt, model, tokenizer)
print("Generated Text:\n", generated_text)

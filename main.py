import wandb

# init wandb
model, arg = '_', '_'
wandb.init(project='nerf', entity='phuber', config=arg)
wandb.watch(model, log='all')

if __name__ == "__main__":
    print("working")
# One Page Trainer
---

* Easy to train classification models to test out state of the art models on CIFAR-10
* Made with the intention of plugging in components for quick tryouts
* EMA Averaging included. The EMA Model usually results in better results if you run for larger number of epochs.

# Results

| Models 						| Accuracy 		| Num of epochs |
| --- 							| --- 			| ---			|
| Resnet18 + Coutout			| 95.67 		| 170 			|
| ShakeShake26-2x32 + Coutout	| 96.00 		| 300 			|

* Stopping training at lower epochs due to time constraints.
* ShakeShake and Cutout is trained till 1800 epochs in the original paper.

Thanks to [owruby](https://github.com/owruby/shake-shake_pytorch) for the shake shake networks and [uoguelph-mlrg](https://github.com/uoguelph-mlrg/Cutout) for the Cutout implementation
# Awesome State-Space Resources for ML

**Contributions are welcome! Please read the [contribution guidelines](#contributions) before contributing.**

## Table of Contents

- [Parameterization and Initialization](#parameterization-and-initialization)
- [Architecture](#architecture)
- [Vision](#vision)
- [Language](#language)
- [Audio](#audio)
- [Time-Series](#time-series)
- [Medical](#medical)
- [Tabular](#tabular)
- [Reinforcement Learning](#reinforcement-learning)
- [Books and Surveys](#books-and-surveys)
- [Tutorials](#tutorials)
- [Miscellaneous](#miscellaneous)

## Parameterization and Initialization
1. [Combining Recurrent, Convolutional, and Continuous-time Models with Linear State-Space Layers](https://arxiv.org/abs/2110.13985) (NeurIPS 2021)
2. [Eﬃciently Modeling Long Sequences with Structured State Spaces](https://arxiv.org/abs/2110.13985) (ICLR 2022)
3. [On the Parameterization and Initialization of Diagonal State Space Models](https://arxiv.org/abs/2206.11893) (NeurIPS 2022)
4. [Diagonal State Spaces are as Effective as Structured State Spaces](https://arxiv.org/abs/2203.14343) (NeurIPS 2022) [[code]](https://github.com/ag1988/dss)
5. [How to Train your HIPPO: State Space Models with Generalized Orthogonal Basis Projections](https://arxiv.org/abs/2206.12037) (ICLR 2023)
6. [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) [[code]](https://github.com/state-spaces/mamba)
7. [Robustifying State-space Models for Long Sequences via Approximate Diagonalization](https://arxiv.org/abs/2310.01698)
8. [StableSSM: Alleviating the Curse of Memory in State-space Models through Stable Reparameterization](https://arxiv.org/abs/2311.14495)
9. [Spectral State Space Models](https://arxiv.org/abs/2312.06837)

## Architecture
1. [S5: Simplified State Space Layers for Sequence Modeling](https://arxiv.org/abs/2208.04933) (ICLR 2023) [[code]](https://github.com/lindermanlab/S5)
2. [Long range language modeling via gated state spaces](https://arxiv.org/abs/2206.13947) (ICLR 2023)
3. [Pretraining Without Attention](https://arxiv.org/abs/2212.10544) [[code]](https://github.com/jxiw/BiGS)
4. [MoE-Mamba: Efficient Selective State Space Models with Mixture of Experts](https://arxiv.org/abs/2401.04081) [[code]](https://github.com/llm-random/llm-random)
5. [LOCOST: State-Space Models for Long Document Abstractive Summarization](https://arxiv.org/abs/2401.17919) [[code]](https://github.com/flbbb/locost-summarization)
6. [BlackMamba: Mixture of Experts for State-Space Models](https://arxiv.org/abs/2402.01771) [[code]](https://github.com/Zyphra/BlackMamba)
7. [DenseMamba: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://arxiv.org/abs/2403.00818) [[code]](https://github.com/WailordHe/DenseSSM)
8. [ZigMa: Zigzag Mamba Diffusion Model](https://arxiv.org/abs/2403.13802) [[code]](https://github.com/CompVis/zigma) [[website]](https://taohu.me/zigma/)
   
## Vision
1. [S4ND: Modeling Images and Videos as Multidimensional Signals with State Spaces](https://arxiv.org/abs/2210.06583) (NeurIPS 2022)
2. [Long movie clip classification with state-space video models](https://arxiv.org/abs/2204.01692) (ECCV 2022) [[code]](https://github.com/md-mohaiminul/ViS4mer)
3. [Efficient Movie Scene Detection using State-Space Transformers](https://arxiv.org/abs/2212.14427) (CVPR 2023)
4. [Selective Structured State-Spaces for Long-Form Video Understanding](https://arxiv.org/abs/2303.14526) (CVPR 2023)
5. [2-D SSM: A General Spatial Layer for Visual Transformers](https://arxiv.org/abs/2306.06635) [[code]](https://github.com/ethanbar11/ssm_2d)
6. [Vision Mamba: Efficient Visual Representation Learning with Bidirectional State Space Model](https://arxiv.org/abs/2401.09417) [[code]](https://github.com/hustvl/Vim)
7. [VMamba: Visual State Space Model](https://arxiv.org/abs/2401.10166) [[code]](https://github.com/MzeroMiko/VMamba)
8. [U-shaped Vision Mamba for Single Image Dehazing](https://arxiv.org/abs/2402.04139) [[code]](https://github.com/zzr-idam/UVM-Net)
9. [Res-VMamba: Fine-Grained Food Category Visual Classification Using Selective State Space Models with Deep Residual Learning](https://arxiv.org/abs/2402.15761) [[code]](https://github.com/ChiShengChen/ResVMamba)
10. [Weak-Mamba-UNet: Visual Mamba Makes CNN and ViT Work Better for Scribble-based Medical Image Segmentation](https://arxiv.org/abs/2402.10887) [[code]](https://github.com/ziyangwang007/Mamba-UNet)
11. [LocalMamba: Visual State Space Model with Windowed Selective Scan](https://arxiv.org/abs/2403.09338) [[code]](https://github.com/hunto/LocalMamba)
12. [Motion Mamba: Efficient and Long Sequence Motion Generation with Hierarchical and Bidirectional Selective SSM](https://arxiv.org/abs/2403.07487) [[code]](https://steve-zeyu-zhang.github.io/MotionMamba/?utm_source=catalyzex.com)

## Language
1. [Hungry Hungry Hippos: Towards Language Modeling with State Space Models](https://arxiv.org/abs/2212.14052) (ICLR 2023) [[code]](https://github.com/HazyResearch/H3)
2. [Long range language modeling via gated state spaces](https://arxiv.org/abs/2206.13947) (ICLR 2023) [[code]](https://github.com/lucidrains/gated-state-spaces-pytorch.git)
3. [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) [[code]](https://github.com/state-spaces/mamba)
4. [MambaByte: Token-free Selective State Space Model](https://arxiv.org/abs/2401.13660) [[code]](https://github.com/lucidrains/MEGABYTE-pytorch)
5. [Can Mamba Learn How to Learn? A Comparative Study on In-Context Learning Tasks](https://arxiv.org/abs/2402.04248)

## Audio
1. [It's Raw! Audio Generation with State-Space Models](https://arxiv.org/abs/2202.09729) (ICML 2022) [[code]](https://github.com/state-spaces/s4)
2. [Augmenting conformers with structured state space models for online speech recognition](https://arxiv.org/abs/2309.08551)
3. [Diagonal State Space Augmented Transformers for Speech Recognition](https://arxiv.org/abs/2302.14120)
4. [Structured State Space Decoder for Speech Recognition and Synthesis](https://arxiv.org/abs/2210.17098)
5. [Spiking Structured State Space Model for Monaural Speech Enhancement](https://arxiv.org/abs/2309.03641)
6. [A Neural State-Space Model Approach to Efficient Speech Separation](https://arxiv.org/abs/2305.16932)
7. [Multi-Head State Space Model for Speech Recognition](https://arxiv.org/abs/2305.12498)
8. [SSAMBA: Self-Supervised Audio Representation Learning with Mamba State Space Model](https://arxiv.org/abs/2405.11831) [[code]](https://github.com/SiavashShams/ssamba)

## Time-Series
1. [Deep State Space Models for Time Series Forecasting](https://papers.nips.cc/paper_files/paper/2018/hash/5cf68969fb67aa6082363a6d4e6468e2-Abstract.html) (NeurIPS 2018)
2. [FiLM: Frequency improved Legendre Memory Model for Long-term Time Series Forecasting](https://arxiv.org/abs/2205.08897) (NeurIPS 2022)
3. [Effectively modeling time series with simple discrete state spaces](https://arxiv.org/abs/2303.09489) (ICLR 2023)
4. [Deep Latent State Space Models for Time-Series Generation](https://arxiv.org/abs/2212.12749) (ICML 2023)
5. [Generative AI for End-to-End Limit Order Book Modelling](https://arxiv.org/abs/2309.00638) (ICAIF 2023)
6. [On the Performance of Legendre State-Space Models in Short-Term Time Series Forecasting](https://ieeexplore.ieee.org/document/10289082) (CCECE 2023)
7. [Neural Continuous-Discrete State Space Models for Irregularly-Sampled Time Series](https://arxiv.org/abs/2301.11308)
8. [Diffusion-based Time Series Imputation and Forecasting with Structured State Space Models](https://arxiv.org/abs/2208.09399)

## Medical
1. [Structured State Space Models for Multiple Instance Learning in Digital Pathology](https://arxiv.org/abs/2306.15789)
2. [Modeling Multivariate Biosignals with Graph Neural Networks and Structured State Space](https://arxiv.org/abs/2211.11176)
3. [Diffusion-based conditional ECG generation with structured state space models](https://arxiv.org/abs/2301.08227)
4. [Improving the Diagnosis of Psychiatric Disorders with Self-Supervised Graph State Space Models](https://arxiv.org/abs/2206.03331)
5. [fMRI-S4: learning short- and long-range dynamic fMRI dependencies using 1D Convolutions and State Space Models](https://arxiv.org/abs/2208.04166)
6. [Vivim: a Video Vision Mamba for Medical Video Object Segmentation](https://arxiv.org/abs/2401.14168) [[code]](https://github.com/scott-yjyang/Vivim)
7. [MambaMorph: a Mamba-based Backbone with Contrastive Feature Learning for Deformable MR-CT Registration](https://arxiv.org/abs/2401.13934) [[code]](https://github.com/Guo-Stone/MambaMorph)
8. [SegMamba: Long-range Sequential Modeling Mamba For 3D Medical Image Segmentation](https://arxiv.org/abs/2401.13560) [[code]](https://github.com/ge-xing/SegMamba)
9. [U-Mamba: Enhancing Long-range Dependency for Biomedical Image Segmentation](https://arxiv.org/abs/2401.04722) [[code]](https://github.com/bowang-lab/U-Mamba)
10. [nnMamba: 3D Biomedical Image Segmentation, Classification and Landmark Detection with State Space Model](https://arxiv.org/abs/2402.03526)
11. [VM-UNet: Vision Mamba UNet for Medical Image Segmentation](https://arxiv.org/abs/2402.02491)
12. [MambaMIR: An Arbitrary-Masked Mamba for Joint Medical Image Reconstruction and Uncertainty Estimation](https://arxiv.org/abs/2402.18451)
13. [ViM-UNet: Vision Mamba for Biomedical Segmentation](https://doi.org/10.48550/arXiv.2404.07705) (MIDL 2024)

## Tabular
1. [MambaTab: A Simple Yet Effective Approach for Handling Tabular Data](https://arxiv.org/abs/2401.08867)

## Reinforcement Learning
1. [Decision S4: Efficient Sequence-Based RL via State Spaces Layers](https://arxiv.org/abs/2306.05167) (ICLR 2023)
2. [Structured State Space Models for In-Context Reinforcement Learning](https://arxiv.org/abs/2303.03982) (NeurIPS 2023)
3. [Mastering Memory Tasks with World Models](https://openreview.net/forum?id=1vDArHJ68h) (ICLR 2024 oral)

## Books and Surveys
1. [Linear State-Space Control Systems](https://onlinelibrary.wiley.com/doi/book/10.1002/9780470117873)
2. [Modeling Sequences with Structured State Spaces](https://www.proquest.com/docview/2880853867?pq-origsite=gscholar&fromopenview=true&sourcetype=Dissertations%20&%20Theses)
3. [Principles of System Identification Theory and Practice](https://www.taylorfrancis.com/books/mono/10.1201/9781315222509/principles-system-identification-arun-tangirala)

## Tutorials
1. [The Annotated S4](https://srush.github.io/annotated-s4/)
2. [The Annotated Mamba](https://srush.github.io/annotated-mamba/hard.html) [[code]](https://github.com/srush/annotated-mamba)
3. [A Visual Guide to Mamba and State Space Models](https://open.substack.com/pub/maartengrootendorst/p/a-visual-guide-to-mamba-and-state)

## Miscellaneous
1. [Variational learning for switching state-space models](https://www.cs.toronto.edu/~hinton/absps/switch.pdf) (Neural Computation 2000)
2. [Liquid structural state-space models](https://arxiv.org/abs/2209.12951) (ICLR 2023)
3. [Resurrecting Recurrent Neural Networks for Long Sequences](https://arxiv.org/abs/2303.06349) (ICML 2023)
4. [Learning Low Dimensional State Spaces with Overparameterized Recurrent Neural Nets](https://arxiv.org/abs/2210.14064) (ICLR 2023)
5. [Block-State Transformers](https://arxiv.org/abs/2306.09539)
6. [Simplifying and Understanding State Space Models with Diagonal Linear RNNs](https://arxiv.org/abs/2212.00768)
7. [Never Train from Scratch: Fair Comparison Of Long- Sequence Models Requires Data-Driven Pirors](https://arxiv.org/abs/2310.02980)
8. [Structured state-space models are deep Wiener models](https://arxiv.org/abs/2312.06211)
9. [Efficient Long Sequence Modeling via State Space Augmented Transformer](https://arxiv.org/abs/2212.08136)
10. [State-space Models with Layer-wise Nonlinearity are Universal Approximators with Exponential Decaying Memory](https://arxiv.org/abs/2309.13414)
11. [Repeat After Me: Transformers are Better than State Space Models at Copying](https://arxiv.org/abs/2402.01032)
12. [Theoretical Foundations of Deep Selective State-Space Models](https://arxiv.org/abs/2402.19047)
13. [The Hidden Attention of Mamba Models](https://arxiv.org/abs/2403.01590)



## Contributions

🎉 Thank you for considering contributing to our Awesome State Space Models for Machine Learning repository! 🚀

### Contribute in 3 Steps:

1. **Fork the Repo:**
   Fork this repo to your GitHub account.

2. **Edit Content:**
   Contribute by adding new resources or improving existing content in the `README.md` file.

3. **Create a Pull Request:**
   Open a pull request (PR) from your branch to the main repository.

### Guidelines

- Follow the existing structure and formatting.
- Ensure added resources are relevant to State Space Models in Machine Learning.
- Verify that links work correctly.

### Reporting Issues

If you encounter issues or have suggestions, open an issue on the GitHub repository.

Your contributions make this repository awesome! Thank you! 🙌

## License

This project is licensed under the [MIT License](LICENSE).

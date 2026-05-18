# Awesome State-Space Resources for ML

**Contributions are welcome! Please read the [contribution guidelines](#contributions) before contributing.**

## Table of Contents

- [Tutorials](#tutorials)  
- [Surveys](#surveys)  
- [Books](#books)  
- [Foundation](#foundation)  
- [Distillation](#distillation)  
- [Architectures](#architectures)  
- [Related Efficient Sequence Models](#related-efficient-sequence-models)  
- [Parameterization and Initialization](#ssm-parameterization-and-initialization)  
- [Systems Optimizations](#systems-optimizations)  
- [Vision](#vision)  
- [Language](#language)  
- [Audio](#audio)  
- [Time-Series](#time-series)  
- [Medical](#medical)  
- [Genomics / Biology](#genomics--biology)  
- [Tabular](#tabular)  
- [Reinforcement Learning](#reinforcement-learning)  

## Tutorials <a name="tutorials"></a>

#### Blogposts
1. [S4 Series](https://hazyresearch.stanford.edu/blog/2022-01-14-s4-1)
2. [The Annotated S4](https://srush.github.io/annotated-s4/)
3. [The Annotated S4D](https://srush.github.io/annotated-s4/s4d.html)
4. [The Annotated Mamba](https://srush.github.io/annotated-mamba/hard.html) [[code]](https://github.com/srush/annotated-mamba)
5. [Mamba: The Easy Way](https://jackcook.com/2024/02/23/mamba.html)
6. [A Visual Guide to Mamba and State Space Models](https://open.substack.com/pub/maartengrootendorst/p/a-visual-guide-to-mamba-and-state)
7. [State Space Models: A Modern Approach](https://probml.github.io/ssm-book/root.html)
8. [Mamba No. 5 (A Little Bit Of...)](https://jameschen.io/jekyll/update/2024/02/12/mamba.html)
9. [Mamba: SSM, Theory, and Implementation in Keras and TensorFlow](https://medium.com/towards-data-science/mamba-ssm-theory-and-implementation-in-keras-and-tensorflow-32d6d4b32546)

#### Videos
1. [Efficiently Modeling Long Sequences with Structured State Spaces](https://www.youtube.com/watch?v=luCBXCErkCs)
2. [Do we need Attention? A Mamba Primer](https://www.youtube.com/watch?v=dVH1dRoMPBc)
3. [Mamba and S4 Explained: Architecture, Parallel Scan, Kernel Fusion, Recurrent, Convolution, Math](https://www.youtube.com/watch?v=8Q_tqwpTpVU)
4. [MAMBA from Scratch](https://www.youtube.com/watch?v=N6Piou4oYx8)
5. [Yannic Kilcher's Video](https://www.youtube.com/watch?v=9dSkvxS2EB0)

## Surveys (Structured State Space Models) <a name="surveys"></a>
1. [Modeling Sequences with Structured State Spaces](https://www.proquest.com/docview/2880853867?pq-origsite=gscholar&fromopenview=true&sourcetype=Dissertations%20&%20Theses)
2. [State Space Models as Foundation Models: A Control Theoretic Overview](https://arxiv.org/abs/2403.16899)
3. [State Space Model for New-Generation Network Alternative to Transformers](https://arxiv.org/abs/2404.09516)
4. [A Survey on Visual Mamba](https://arxiv.org/abs/2404.15956)
5. [Mamba-360: Survey of State Space Models as Transformer Alternative for Long Sequence Modelling: Methods, Applications, and Challenges](https://arxiv.org/abs/2404.16112)
6. [A Survey on Structured State Space Sequence (S4) Models](https://arxiv.org/abs/2503.18970)

## Books (Classical State Space Models) <a name="books"></a>
1. [Linear State-Space Control Systems](https://onlinelibrary.wiley.com/doi/book/10.1002/9780470117873)
2. [Principles of System Identification Theory and Practice](https://www.taylorfrancis.com/books/mono/10.1201/9781315222509/principles-system-identification-arun-tangirala)

## Foundation
### Core Mamba Lineage
1. [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) [[code]](https://github.com/state-spaces/mamba)
2. [Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality](https://arxiv.org/abs/2405.21060) (Mamba-2 / SSD)
3. [Mamba-3: Improved Sequence Modeling using State Space Principles](https://arxiv.org/abs/2603.15569)

### Theory, Analysis, and Limitations
1. [Learning Low Dimensional State Spaces with Overparameterized Recurrent Neural Nets](https://arxiv.org/abs/2210.14064) (ICLR 2023)
2. [Simplifying and Understanding State Space Models with Diagonal Linear RNNs](https://arxiv.org/abs/2212.00768)
3. [State-space Models with Layer-wise Nonlinearity are Universal Approximators with Exponential Decaying Memory](https://arxiv.org/abs/2309.13414)
4. [Never Train from Scratch: Fair Comparison of Long-Sequence Models Requires Data-Driven Priors](https://arxiv.org/abs/2310.02980)
5. [Structured state-space models are deep Wiener models](https://arxiv.org/abs/2312.06211)
6. [Repeat After Me: Transformers are Better than State Space Models at Copying](https://arxiv.org/abs/2402.01032)
7. [Can Mamba Learn How to Learn? A Comparative Study on In-Context Learning Tasks](https://arxiv.org/abs/2402.04248)
8. [Theoretical Foundations of Deep Selective State-Space Models](https://arxiv.org/abs/2402.19047)
9. [The Hidden Attention of Mamba Models](https://arxiv.org/abs/2403.01590)
10. [The Illusion of State in State-Space Models](https://arxiv.org/abs/2404.08819)
11. [The Expressive Capacity of State Space Models: A Formal Language Perspective](https://arxiv.org/abs/2405.17394)
12. [An Empirical Study of Mamba-based Language Models](https://arxiv.org/abs/2406.07887)
13. [Longhorn: State Space Models are Amortized Online Learners](https://arxiv.org/abs/2407.14207)
14. [Understanding the Skill Gap in Recurrent Language Models: The Role of the Gather-and-Aggregate Mechanism](https://arxiv.org/abs/2504.18574)

## Distillation
1. [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://arxiv.org/abs/2408.10189) [[code]](https://github.com/goombalab/phi-mamba)
2. [The Mamba in the Llama: Distilling and Accelerating Hybrid Models](https://arxiv.org/abs/2408.15237)
3. [Thinking Slow, Fast: Scaling Inference Compute with Distilled Reasoners](https://arxiv.org/abs/2502.20339)
4. [Retrieval-Aware Distillation for Transformer-SSM Hybrids](https://arxiv.org/abs/2602.11374)

## Architectures

### Core SSM / Mamba Architectures
1. [Long range language modeling via gated state spaces](https://arxiv.org/abs/2206.13947) (ICLR 2023)
2. [S5: Simplified State Space Layers for Sequence Modeling](https://arxiv.org/abs/2208.04933) (ICLR 2023) [[code]](https://github.com/lindermanlab/S5)
3. [Liquid structural state-space models](https://arxiv.org/abs/2209.12951) (ICLR 2023)
4. [Pretraining Without Attention](https://arxiv.org/abs/2212.10544) [[code]](https://github.com/jxiw/BiGS)
5. [MoE-Mamba: Efficient Selective State Space Models with Mixture of Experts](https://arxiv.org/abs/2401.04081) [[code]](https://github.com/llm-random/llm-random)
6. [BlackMamba: Mixture of Experts for State-Space Models](https://arxiv.org/abs/2402.01771) [[code]](https://github.com/Zyphra/BlackMamba)
7. [Mamba-ND: Selective State Space Modeling for Multi-Dimensional Data](https://arxiv.org/abs/2402.05892)
8. [DenseMamba: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://arxiv.org/abs/2403.00818) [[code]](https://github.com/WailordHe/DenseSSM)
9. [S7: Selective and Simplified State Space Layers for Sequence Modeling](https://arxiv.org/abs/2410.03464)
10. [Sparsified State-Space Models are Efficient Highway Networks](https://arxiv.org/abs/2505.20698) [[code]](https://github.com/woominsong/Simba)
11. [Routing Mamba: Scaling State Space Models with Mixture-of-Experts Projection](https://arxiv.org/abs/2506.18145)

### Hybrid SSM-Transformer Architectures
1. [Efficient Long Sequence Modeling via State Space Augmented Transformer](https://arxiv.org/abs/2212.08136)
2. [Block-State Transformers](https://arxiv.org/abs/2306.09539)
3. [Jamba: A Hybrid Transformer-Mamba Language Model](https://arxiv.org/abs/2403.19887)
4. [Zamba: A Compact 7B SSM Hybrid Model](https://arxiv.org/abs/2405.16712)
5. [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://arxiv.org/abs/2406.07522)
6. [Jamba-1.5: Hybrid Transformer-Mamba Models at Scale](https://arxiv.org/abs/2408.12570)
7. [Hymba: A Hybrid-head Architecture for Small Language Models](https://arxiv.org/abs/2411.13676)
8. [The Zamba2 Suite: Technical Report](https://arxiv.org/abs/2411.15242)
9. [Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models](https://arxiv.org/abs/2504.03624)

## Related Efficient Sequence Models
> Non-SSM or loosely related efficient sequence models commonly compared with SSMs, Mamba, and other recurrent or linear-time architectures.

1. [Mega: Moving Average Equipped Gated Attention](https://arxiv.org/abs/2209.10655)
2. [Hyena Hierarchy: Towards Larger Convolutional Language Models](https://arxiv.org/abs/2302.10866)
3. [Resurrecting Recurrent Neural Networks for Long Sequences](https://arxiv.org/abs/2303.06349) (ICML 2023)
4. [RWKV: Reinventing RNNs for the Transformer Era](https://arxiv.org/abs/2305.13048)
5. [Retentive Network: A Successor to Transformer for Large Language Models](https://arxiv.org/abs/2307.08621)
6. [Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models](https://arxiv.org/abs/2402.19427)
7. [xLSTM: Extended Long Short-Term Memory](https://arxiv.org/abs/2405.04517)
8. [Explaining Modern Gated-Linear RNNs via a Unified Implicit Attention Formulation](https://arxiv.org/abs/2405.16504)
9. [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://arxiv.org/abs/2412.06464)
10. [Raven: High-Recall Sequence Modeling with Sparse Memory Routing](https://github.com/goombalab/raven/blob/main/raven.pdf) [[code]](https://github.com/goombalab/raven)
11. [Kimi Linear: An Expressive, Efficient Attention Architecture](https://arxiv.org/abs/2510.26692) [[code]](https://github.com/MoonshotAI/Kimi-Linear)

## SSM Parameterization and Initialization
1. [Legendre Memory Units: Continuous-Time Representation in Recurrent Neural Networks](https://papers.nips.cc/paper_files/paper/2019/hash/952285b9b7e7a1be5aa7849f32ffff05-Abstract.html) (NeurIPS 2019)
2. [HiPPO: Recurrent Memory with Optimal Polynomial Projections](https://arxiv.org/abs/2008.07669)
3. [Combining Recurrent, Convolutional, and Continuous-time Models with Linear State-Space Layers](https://arxiv.org/abs/2110.13985) (NeurIPS 2021)
4. [Efficiently Modeling Long Sequences with Structured State Spaces](https://arxiv.org/abs/2111.00396) (ICLR 2022)
5. [Diagonal State Spaces are as Effective as Structured State Spaces](https://arxiv.org/abs/2203.14343) (NeurIPS 2022) [[code]](https://github.com/ag1988/dss)
6. [On the Parameterization and Initialization of Diagonal State Space Models](https://arxiv.org/abs/2206.11893) (NeurIPS 2022)
7. [How to Train your HIPPO: State Space Models with Generalized Orthogonal Basis Projections](https://arxiv.org/abs/2206.12037) (ICLR 2023)
8. [Robustifying State-space Models for Long Sequences via Approximate Diagonalization](https://arxiv.org/abs/2310.01698)
9. [StableSSM: Alleviating the Curse of Memory in State-space Models through Stable Reparameterization](https://arxiv.org/abs/2311.14495)
10. [Spectral State Space Models](https://arxiv.org/abs/2312.06837)
11. [From Generalization Analysis to Optimization Designs for State Space Models](https://arxiv.org/abs/2405.02670) (ICML 2024)

## Systems Optimizations
1. [Quamba: A Post-Training Quantization Recipe for Selective State Space Models](https://arxiv.org/abs/2410.13229)
2. [Marconi: Prefix Caching for the Era of Hybrid LLMs](https://arxiv.org/abs/2411.19379) (MLSys 2025)
3. [MambaQuant: Quantizing the Mamba Family with Variance Aligned Rotation Methods](https://arxiv.org/abs/2501.13484)
4. [Mamba Drafters for Speculative Decoding](https://arxiv.org/abs/2506.01206)

## Vision
1. [Long movie clip classification with state-space video models](https://arxiv.org/abs/2204.01692) (ECCV 2022) [[code]](https://github.com/md-mohaiminul/ViS4mer)
2. [S4ND: Modeling Images and Videos as Multidimensional Signals with State Spaces](https://arxiv.org/abs/2210.06583) (NeurIPS 2022)
3. [Efficient Movie Scene Detection using State-Space Transformers](https://arxiv.org/abs/2212.14427) (CVPR 2023)
4. [Selective Structured State-Spaces for Long-Form Video Understanding](https://arxiv.org/abs/2303.14526) (CVPR 2023)
5. [2-D SSM: A General Spatial Layer for Visual Transformers](https://arxiv.org/abs/2306.06635) [[code]](https://github.com/ethanbar11/ssm_2d)
6. [Vision Mamba: Efficient Visual Representation Learning with Bidirectional State Space Model](https://arxiv.org/abs/2401.09417) [[code]](https://github.com/hustvl/Vim)
7. [VMamba: Visual State Space Model](https://arxiv.org/abs/2401.10166) [[code]](https://github.com/MzeroMiko/VMamba)
8. [U-shaped Vision Mamba for Single Image Dehazing](https://arxiv.org/abs/2402.04139) [[code]](https://github.com/zzr-idam/UVM-Net)
9. [State Space Models for Event Cameras](https://arxiv.org/abs/2402.15584) [[code]](https://github.com/uzh-rpg/ssms_event_cameras) (CVPR 2024 Spotlight)
10. [MambaIR: A Simple Baseline for Image Restoration with State-Space Model](https://arxiv.org/abs/2402.15648)
11. [Res-VMamba: Fine-Grained Food Category Visual Classification Using Selective State Space Models with Deep Residual Learning](https://arxiv.org/abs/2402.15761) [[code]](https://github.com/ChiShengChen/ResVMamba)
12. [VideoMamba: State Space Model for Efficient Video Understanding](https://arxiv.org/abs/2403.06977)
13. [Motion Mamba: Efficient and Long Sequence Motion Generation with Hierarchical and Bidirectional Selective SSM](https://arxiv.org/abs/2403.07487) [[code]](https://steve-zeyu-zhang.github.io/MotionMamba/)
14. [LocalMamba: Visual State Space Model with Windowed Selective Scan](https://arxiv.org/abs/2403.09338) [[code]](https://github.com/hunto/LocalMamba)
15. [MambaTalk: Efficient Holistic Gesture Synthesis with Selective State Space Models](https://arxiv.org/abs/2403.09471) [[code]](https://github.com/kkakkkka/MambaTalk)
16. [ZigMa: Zigzag Mamba Diffusion Model](https://arxiv.org/abs/2403.13802) (ECCV 2024) [[code]](https://github.com/CompVis/zigma) [[website]](https://taohu.me/zigma/)
17. [MambaOut: Do We Really Need Mamba for Vision?](https://arxiv.org/abs/2405.07992)
18. [SUM: Saliency Unification through Mamba for Visual Attention Modeling](https://arxiv.org/abs/2406.17815) [[code]](https://github.com/Arhosseini77/SUM)
19. [MambaVision: A Hybrid Mamba-Transformer Vision Backbone](https://arxiv.org/abs/2407.08083)
20. [DynamicVis: An Efficient and General Visual Foundation Model for Remote Sensing Image Understanding](https://arxiv.org/abs/2503.16426) [[code]](https://github.com/KyanChen/DynamicVis)

## Language
1. [Hungry Hungry Hippos: Towards Language Modeling with State Space Models](https://arxiv.org/abs/2212.14052) (ICLR 2023) [[code]](https://github.com/HazyResearch/H3)
2. [MambaByte: Token-free Selective State Space Model](https://arxiv.org/abs/2401.13660) [[code]](https://github.com/lucidrains/MEGABYTE-pytorch)
3. [LOCOST: State-Space Models for Long Document Abstractive Summarization](https://arxiv.org/abs/2401.17919) [[code]](https://github.com/flbbb/locost-summarization)
4. [Falcon Mamba: The First Competitive Attention-free 7B Language Model](https://arxiv.org/abs/2410.05355)
5. [Llamba: Scaling Distilled Recurrent Models for Efficient Language Processing](https://arxiv.org/abs/2502.14458)
6. [LongMamba: Enhancing Mamba's Long Context Capabilities via Training-Free Receptive Field Enlargement](https://arxiv.org/abs/2504.16053)

## Audio
1. [It's Raw! Audio Generation with State-Space Models](https://arxiv.org/abs/2202.09729) (ICML 2022) [[code]](https://github.com/state-spaces/s4)
2. [Structured State Space Decoder for Speech Recognition and Synthesis](https://arxiv.org/abs/2210.17098)
3. [Diagonal State Space Augmented Transformers for Speech Recognition](https://arxiv.org/abs/2302.14120)
4. [Multi-Head State Space Model for Speech Recognition](https://arxiv.org/abs/2305.12498)
5. [A Neural State-Space Model Approach to Efficient Speech Separation](https://arxiv.org/abs/2305.16932)
6. [Spiking Structured State Space Model for Monaural Speech Enhancement](https://arxiv.org/abs/2309.03641)
7. [Augmenting conformers with structured state space models for online speech recognition](https://arxiv.org/abs/2309.08551)
8. [Dual-path Mamba: Short and Long-term Bidirectional Selective Structured State Space Models for Speech Separation](https://arxiv.org/abs/2403.18257) [[code]](https://github.com/xi-j/Mamba-TasNet)
9. [SSAMBA: Self-Supervised Audio Representation Learning with Mamba State Space Model](https://arxiv.org/abs/2405.11831) [[code]](https://github.com/SiavashShams/ssamba)
10. [Audio Mamba: Bidirectional State Space Model for Audio Representation Learning](https://arxiv.org/abs/2406.03344) [[code]](https://github.com/kaistmm/Audio-Mamba-AuM)
11. [Speech Slytherin: Examining the Performance and Efficiency of Mamba for Speech Separation, Recognition, and Synthesis](https://arxiv.org/abs/2407.09732) [[code]](https://github.com/xi-j/Mamba-ASR)

## Time-Series
1. [Deep Kalman Filters](https://arxiv.org/abs/1511.05121)
2. [Deep Variational Bayes Filters: Unsupervised Learning of State Space Models from Raw Data](https://arxiv.org/abs/1605.06432)
3. [Structured Inference Networks for Nonlinear State Space Models](https://arxiv.org/abs/1609.09869)
4. [Deep State Space Models for Time Series Forecasting](https://papers.nips.cc/paper_files/paper/2018/hash/5cf68969fb67aa6082363a6d4e6468e2-Abstract.html) (NeurIPS 2018)
5. [FiLM: Frequency improved Legendre Memory Model for Long-term Time Series Forecasting](https://arxiv.org/abs/2205.08897) (NeurIPS 2022)
6. [Diffusion-based Time Series Imputation and Forecasting with Structured State Space Models](https://arxiv.org/abs/2208.09399)
7. [Deep Latent State Space Models for Time-Series Generation](https://arxiv.org/abs/2212.12749) (ICML 2023)
8. [Neural Continuous-Discrete State Space Models for Irregularly-Sampled Time Series](https://arxiv.org/abs/2301.11308)
9. [Effectively modeling time series with simple discrete state spaces](https://arxiv.org/abs/2303.09489) (ICLR 2023)
10. [Generative AI for End-to-End Limit Order Book Modelling](https://arxiv.org/abs/2309.00638) (ICAIF 2023)
11. [On the Performance of Legendre State-Space Models in Short-Term Time Series Forecasting](https://ieeexplore.ieee.org/document/10289082) (CCECE 2023)
12. [Is Mamba Effective for Time Series Forecasting?](https://arxiv.org/abs/2403.11144)

## Medical
1. [Improving the Diagnosis of Psychiatric Disorders with Self-Supervised Graph State Space Models](https://arxiv.org/abs/2206.03331)
2. [fMRI-S4: learning short- and long-range dynamic fMRI dependencies using 1D Convolutions and State Space Models](https://arxiv.org/abs/2208.04166)
3. [Modeling Multivariate Biosignals with Graph Neural Networks and Structured State Space](https://arxiv.org/abs/2211.11176)
4. [Diffusion-based conditional ECG generation with structured state space models](https://arxiv.org/abs/2301.08227)
5. [Structured State Space Models for Multiple Instance Learning in Digital Pathology](https://arxiv.org/abs/2306.15789)
6. [U-Mamba: Enhancing Long-range Dependency for Biomedical Image Segmentation](https://arxiv.org/abs/2401.04722) [[code]](https://github.com/bowang-lab/U-Mamba)
7. [SegMamba: Long-range Sequential Modeling Mamba For 3D Medical Image Segmentation](https://arxiv.org/abs/2401.13560) [[code]](https://github.com/ge-xing/SegMamba)
8. [MambaMorph: a Mamba-based Backbone with Contrastive Feature Learning for Deformable MR-CT Registration](https://arxiv.org/abs/2401.13934) [[code]](https://github.com/Guo-Stone/MambaMorph)
9. [Vivim: a Video Vision Mamba for Medical Video Object Segmentation](https://arxiv.org/abs/2401.14168) [[code]](https://github.com/scott-yjyang/Vivim)
10. [VM-UNet: Vision Mamba UNet for Medical Image Segmentation](https://arxiv.org/abs/2402.02491)
11. [nnMamba: 3D Biomedical Image Segmentation, Classification and Landmark Detection with State Space Model](https://arxiv.org/abs/2402.03526)
12. [Weak-Mamba-UNet: Visual Mamba Makes CNN and ViT Work Better for Scribble-based Medical Image Segmentation](https://arxiv.org/abs/2402.10887) [[code]](https://github.com/ziyangwang007/Mamba-UNet)
13. [MambaMIR: An Arbitrary-Masked Mamba for Joint Medical Image Reconstruction and Uncertainty Estimation](https://arxiv.org/abs/2402.18451)
14. [ViM-UNet: Vision Mamba for Biomedical Segmentation](https://arxiv.org/abs/2404.07705) (MIDL 2024)
15. [I2I-Mamba: Multi-modal medical image synthesis via selective state space modeling](https://arxiv.org/abs/2405.14022) [[code]](https://github.com/icon-lab/I2I-Mamba)
16. [BioMamba: A Pre-trained Biomedical Language Representation Model Leveraging Mamba](https://arxiv.org/abs/2408.02600)
17. [MambaRoll: Physics-Driven Autoregressive State Space Models for Medical Image Reconstruction](https://arxiv.org/abs/2412.09331) [[code]](https://github.com/icon-lab/MambaRoll)

## Genomics / Biology
1. [Caduceus: Bi-Directional Equivariant Long-Range DNA Sequence Modeling](https://arxiv.org/abs/2403.03234)

## Tabular
1. [MambaTab: A Plug-and-Play Model for Learning Tabular Data](https://arxiv.org/abs/2401.08867)
2. [Mambular: A Sequential Model for Tabular Deep Learning](https://arxiv.org/abs/2408.06291)

## Reinforcement Learning
1. [Structured State Space Models for In-Context Reinforcement Learning](https://arxiv.org/abs/2303.03982) (NeurIPS 2023)
2. [Decision S4: Efficient Sequence-Based RL via State Spaces Layers](https://arxiv.org/abs/2306.05167) (ICLR 2023)
3. [Mastering Memory Tasks with World Models](https://openreview.net/forum?id=1vDArHJ68h) (ICLR 2024 oral)

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

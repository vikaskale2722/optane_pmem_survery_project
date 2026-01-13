# Intel Optane Persistent Memory Survey Project

## 📖 Project Overview

This repository contains a comprehensive survey and research project focused on **Intel Optane Persistent Memory (PMem)** technology. The project explores the architecture, applications, performance characteristics, and research landscape surrounding persistent memory systems, particularly Intel's Optane DC Persistent Memory Modules.

Intel Optane PMem represents a revolutionary memory technology that bridges the gap between volatile DRAM and non-volatile storage, offering:
- **Byte-addressable persistence**: Direct access like DRAM with storage-like durability
- **Large capacity**: Higher capacity than traditional DRAM at lower cost per GB
- **Low latency**: Significantly faster than SSDs while maintaining persistence
- **Memory tiering**: Creates a new tier in the memory hierarchy between DRAM and storage

This survey project aims to provide a comprehensive analysis of the current research, practical applications, and future directions of persistent memory technology.

---

## Project Objectives

1. **Systematic Literature Review**: Conduct a thorough survey of academic papers, industry reports, and technical documentation related to Intel Optane PMem
2. **Technology Analysis**: Analyze the architecture, programming models, and performance characteristics of persistent memory systems
3. **Application Domain Study**: Investigate use cases across databases, file systems, in-memory computing, and cloud infrastructure
4. **Benchmarking & Evaluation**: Review performance studies and comparative analyses of PMem vs. traditional memory/storage
5. **Research Synthesis**: Identify research gaps, challenges, and future opportunities in the persistent memory domain

---

## Repository Structure

```
optane_pmem_survery_project/
│
├── Filtered First List and Information Extraction/
│   └── Contains initial filtered research papers and extracted key information
│
├── Project Plan and Milestones/
│   └── Project timeline, milestones, and progress tracking documents
│
├── Research Paper - Drafts and Resources/
│   └── Draft versions of the survey paper and supporting materials
│
├── Research Paper Scrapping/
│   └── Scripts and tools for automated paper collection and metadata extraction
│
├── Research Papers to Study - Sorted/
│   └── Curated and categorized collection of relevant research papers
│
└── README.md
    └── This file
```

### Directory Descriptions

#### `Filtered First List and Information Extraction/`
Contains the initial curated list of research papers relevant to Intel Optane PMem, along with extracted metadata such as:
- Paper titles, authors, and publication venues
- Key contributions and findings
- Categorization by research domain (e.g., databases, file systems, operating systems)
- Citation information and relevance scores

#### `Project Plan and Milestones/`
Includes project management documents detailing:
- Project timeline and deadlines
- Research methodology and workflow
- Milestone definitions and completion criteria
- Task assignments and progress tracking

#### `Research Paper - Drafts and Resources/`
Houses the evolving survey paper, including:
- LaTeX source files for the research paper
- Draft versions and revision history
- Supplementary materials (figures, tables, diagrams)
- Bibliography and reference management files

#### `Research Paper Scrapping/`
Contains Python scripts and tools for:
- Automated paper discovery from academic databases (IEEE Xplore, ACM Digital Library, arXiv)
- Metadata extraction and parsing
- PDF processing and text extraction
- Citation network analysis

#### `Research Papers to Study - Sorted/`
Organized collection of papers categorized by:
- **Architecture & Hardware**: PMem module design, memory controllers, persistence mechanisms
- **Programming Models**: PMDK, file systems (PMFS, NOVA), transactional memory
- **Database Systems**: In-memory databases, persistent indexes, recovery protocols
- **Operating Systems**: Kernel support, memory management, crash consistency
- **Applications**: Analytics, machine learning, graph processing, key-value stores
- **Performance Analysis**: Benchmarking studies, comparative evaluations

---

## Research Scope

### Key Topics Covered

1. **Persistent Memory Technology**
   - Intel Optane DC Persistent Memory architecture
   - 3D XPoint technology fundamentals
   - Memory modes: App Direct vs. Memory Mode
   - Hardware characteristics and limitations

2. **Programming Models & Software Stack**
   - Persistent Memory Development Kit (PMDK)
   - File systems: PMFS, NOVA, Ext4-DAX, XFS-DAX
   - Memory allocation libraries: libpmem, libpmemobj
   - Crash consistency mechanisms

3. **System Integration**
   - Operating system support (Linux kernel, Windows)
   - Memory management and page tables
   - Cache flush instructions (CLFLUSH, CLFLUSHOPT, CLWB)
   - Hardware support (ADR, eADR)

4. **Application Domains**
   - Database systems (SAP HANA, Redis, MongoDB)
   - In-memory analytics and OLAP
   - Key-value stores
   - Machine learning frameworks
   - Graph processing systems

5. **Performance & Benchmarking**
   - Latency and bandwidth analysis
   - Endurance and wear-out studies
   - Comparison with DRAM and NVMe SSDs
   - Real-world workload performance

---

## Tools & Technologies

### Research Tools
- **Paper Management**: Zotero, Mendeley
- **Literature Search**: Google Scholar, Semantic Scholar, arXiv, IEEE Xplore, ACM Digital Library
- **Citation Analysis**: Citation network tools, bibliometric analysis

### Development Tools
- **Programming Languages**: Python, C/C++
- **Document Processing**: LaTeX, BibTeX
- **Data Analysis**: pandas, matplotlib, NumPy
- **Web Scraping**: BeautifulSoup, Selenium, scholarly

### Version Control
- **Git & GitHub**: Source code management and collaboration
- **Markdown**: Documentation and note-taking

---

## Methodology

### Research Process

1. **Paper Discovery Phase**
   - Keyword-based search across academic databases
   - Snowball sampling from reference lists
   - Citation forward/backward tracking
   - Manual curation from conferences (SOSP, OSDI, FAST, ISCA, MICRO, ASPLOS)

2. **Screening & Selection**
   - Initial relevance assessment based on title/abstract
   - Quality evaluation using venue reputation and citation count
   - Full-text review for highly relevant papers
   - Categorization into research themes

3. **Information Extraction**
   - Key contribution identification
   - Methodology and evaluation approach
   - Results and findings summary
   - Open problems and future work

4. **Synthesis & Analysis**
   - Cross-paper comparison and trend analysis
   - Research gap identification
   - Taxonomy development
   - Critical evaluation of the field

5. **Writing & Documentation**
   - Survey paper drafting in LaTeX
   - Section organization: introduction, background, taxonomy, applications, challenges
   - Figure and table creation
   - Citation and bibliography management

---

## Key Research Areas

### 1. **Persistent Memory Architecture**
- Hardware design and memory controller architecture
- Persistence guarantees and failure atomicity
- Memory encryption and security
- Power failure protection (ADR/eADR)

### 2. **Programming Abstractions**
- Transactional memory for PMem
- Persistent data structures (persistent B-trees, hash tables)
- Lock-free and wait-free algorithms
- Failure-atomic regions and logging

### 3. **File System Design**
- DAX-enabled file systems
- Metadata management in PMem
- Consistency protocols (journaling, copy-on-write)
- Hybrid DRAM-PMem architectures

### 4. **Database Systems**
- Recovery mechanisms for persistent memory databases
- Logging and checkpointing strategies
- Index structures optimized for PMem
- HTAP (Hybrid Transactional/Analytical Processing) systems

### 5. **Performance Optimization**
- Cache management and flush optimization
- NUMA-aware PMem access
- Memory bandwidth optimization
- Wear-leveling and endurance management

---

## Getting Started

### Prerequisites

To work with this repository, you'll need:

```bash
# For Python scripts
Python 3.8+
pip install pandas numpy matplotlib beautifulsoup4 requests

# For LaTeX compilation
texlive-full or MiKTeX
```

### Cloning the Repository

```bash
git clone https://github.com/vikaskale2722/optane_pmem_survery_project.git
cd optane_pmem_survery_project
```

### Running Paper Scraping Scripts

```bash
cd "Research Paper Scrapping"
python scrape_papers.py --keywords "optane persistent memory" --max-results 100
```

### Compiling the Survey Paper

```bash
cd "Research Paper - Drafts and Resources"
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

---

## Current Progress

### Milestones Completed
- [x] Initial project setup and repository structure
- [x] Literature search and paper collection
- [x] First-pass filtering and categorization
- [x] Information extraction from key papers
- [x] Complete taxonomy development
- [x] Draft survey sections (in progress)
- [x] Performance analysis synthesis
- [x] Final paper review and submission

---

## Related Resources

### Official Intel Optane Resources
- [Intel Optane Persistent Memory](https://www.intel.com/content/www/us/en/products/details/optane-memory.html)
- [PMDK Documentation](https://pmem.io/)
- [ipmctl GitHub Repository](https://github.com/intel/ipmctl)

### Key Research Groups
- [NVSL at UC San Diego](https://nvsl.ucsd.edu/)
- [Non-Volatile Systems Lab at University of Washington](https://dada.cs.washington.edu/)
- [MIT PDOS](https://pdos.csail.mit.edu/)

### Important Conferences
- SOSP (Symposium on Operating Systems Principles)
- OSDI (USENIX Symposium on Operating Systems Design and Implementation)
- FAST (USENIX Conference on File and Storage Technologies)
- ASPLOS (International Conference on Architectural Support for Programming Languages and Operating Systems)
- ISCA (International Symposium on Computer Architecture)

---

## Contributing

Contributions to this survey project are welcome! If you have:
- Additional relevant papers to include
- Corrections or improvements to documentation
- New categorizations or insights
- Tools for analysis or visualization

Please feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-contribution`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-contribution`)
5. Open a Pull Request

---

## Citation

If you use this survey or find it helpful in your research, please cite:

```bibtex
@misc{kale2024optane,
  author = {Vikas Kale},
  title = {Intel Optane Persistent Memory: A Comprehensive Survey},
  year = {2024},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/vikaskale2722/optane_pmem_survery_project}}
}
```

---

## Contact

**Vikas Kale**
- GitHub: [@vikaskale2722](https://github.com/vikaskale2722)
- Email: vikaskale2722@gmail.com

For questions, suggestions, or collaboration opportunities, feel free to open an issue or reach out directly.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Intel Corporation for developing and open-sourcing Optane PMem tools and documentation
- The PMDK development community
- Researchers and authors of the surveyed papers
- Academic institutions and labs working on persistent memory research

---

## Important Notes

### Intel Optane Business Update (2022)
As of 2022, Intel announced the wind-down of its Optane business. However, the technology and research remain highly relevant:
- Existing Intel Optane products (100 and 200 series) continue to be supported during their product lifetime
- PMDK libraries and tools remain available as open-source projects
- The persistent memory programming model is applicable to emerging CXL-attached memory devices
- Research insights are valuable for next-generation memory technologies

### Repository Status
This is an active research project. Content is continuously being updated and refined as new papers are reviewed and analyzed.

---

**Project Status**: Completed

---

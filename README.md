# CSCI 572: Information Retrieval - Fall 2024

Welcome to the repository for **CSCI 572: Information Retrieval** under Professor **Saty** for **Fall 2024**. This repository contains my assignments for the course, organized by assignment number. Feel free to explore the different assignments to see the implementation of various information retrieval concepts.

## Course Overview

This course covers the fundamental concepts and techniques of information retrieval, including:

- Text processing
- Indexing
- Search algorithms
- Relevance ranking
- Evaluation metrics
- Web search and retrieval
- Clustering and classification techniques

## Repository Structure

The repository is organized as follows:

- **Assignment 1**: [Link to Assignment 1](Assignment%201/)
- **Assignment 2**: [Link to Assignment 2](Assignment%202/)

Each assignment folder contains the relevant code, documentation, and any required datasets.

### Assignment 1: Web Search Engine Comparison

In this assignment, we compare the search results from Google with a different assigned search engine (Bing, Yahoo!, Ask, or DuckDuckGo). The assignment covers:
- Scraping search engine results using a Python script.
- Comparing the overlap of results between Google and the assigned search engine.
- Computing the **percent overlap** and **Spearman's rank correlation coefficient** to analyze the correlation between the rankings of search results.
- Reporting on the performance and similarities between the assigned search engine and Google.

### Assignment 2: Web Crawling

In this assignment, we work with **crawler4j**, a Java-based web crawler, to:
- Crawl a pre-assigned news website (e.g., New York Times, Wall Street Journal, Fox News).
- Configure the crawler to fetch a maximum of 20,000 pages and record the fetched pages' metadata (status codes, file sizes, and content types).
- Analyze the fetched data to collect statistics such as the number of attempted and successful fetches, the number of unique URLs, and file sizes.
- Report the crawl's performance and statistics in various CSV files and a final report.


## Getting Started

### Prerequisites

- Python 3.x
- Required packages can be installed using the provided `requirements.txt` file.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/shaas1704/CSCI-572--Information-Retrieval.git
    ```
2. Navigate to the assignment directory:
    ```bash
    cd CSCI-572--Information-Retrieval/Assignment1
    ```
3. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running Assignments

To run a particular assignment, follow the instructions provided in the respective assignment folder.

# Customer Segmentation — Detailed Report

## Executive Summary

This project applies unsupervised learning to identify natural customer groups from spending data. Using K-Means clustering, we discover 4 distinct customer segments, each with unique purchasing behaviors and characteristics. Unlike supervised learning where we predict a known outcome, clustering reveals hidden patterns without labels.

---

## Problem Statement

**Objective:** Discover natural customer groups based on spending across product categories

**Dataset:** Wholesale Customers Dataset
- 440 customers
- 8 features: spending on Fresh, Milk, Grocery, Frozen, Detergents, Delicatessen, and customer type indicators
- No predefined labels (unsupervised task)
- Mix of retail and wholesale customers

---

## Methodology

### 1. Data Exploration
- Feature distributions (spending amounts)
- Correlation between product categories
- Outlier detection
- Data scale assessment

### 2. Data Preprocessing
- Feature scaling (essential for K-Means, distance-based algorithm)
- Standardization (zero mean, unit variance)
- Handling outliers if present

### 3. Determining Optimal Clusters

**Elbow Method:**
- Fit K-Means for k = 1 to 10
- Calculate within-cluster sum of squares (WCSS)
- Plot WCSS vs. k
- Identify "elbow" point where improvement diminishes

**Gap Statistic:** Alternative method for comparison

### 4. Final Clustering
- K-Means with optimal k
- Multiple runs (random initialization) for stability
- Assign each customer to a cluster

### 5. Cluster Profiling
- Calculate mean feature values per cluster
- Describe characteristics of each segment
- Identify actionable business implications

---

## Key Findings

### A. Optimal Number of Clusters

**Elbow Method Result:** k = 4 clusters
- WCSS reduction plateaus after 4 clusters
- Silhouette score optimal at k = 4
- 4 clusters provide meaningful, interpretable segments

### B. Cluster Profiles

**Cluster 1: Premium Retail Customers (~25% of customers)**
- High spending across all categories
- Especially high: Milk, Grocery, Detergents
- Likely: Retail chains or large stores
- **Strategy:** VIP treatment, volume discounts, dedicated support

**Cluster 2: Budget-Conscious Customers (~40% of customers)**
- Low spending across all categories
- Smallest average order values
- Likely: Small convenience stores, independent retailers
- **Strategy:** Entry-level pricing, bundled offers, relationship building

**Cluster 3: Fresh-Focused Customers (~15% of customers)**
- Very high Fresh product spending
- Low Grocery/Detergents/Milk
- Likely: Farmers markets, specialty fresh stores
- **Strategy:** Premium fresh offerings, seasonal specials, logistics optimization

**Cluster 4: Diversified Customers (~20% of customers)**
- Balanced spending across categories
- Moderate spending levels
- Likely: General grocery stores, supermarkets
- **Strategy:** Cross-category promotions, loyalty programs



### D. Business Insights

1. **Cluster 1 (Premium):** High-value customers worth retaining
   - Risk: Small % of base; losing one = significant impact
   - Opportunity: Premium services, volume incentives

2. **Cluster 2 (Budget):** Largest segment but low value per customer
   - Risk: Price-sensitive; compete on cost
   - Opportunity: Volume discounts, long-term relationships

3. **Cluster 3 (Fresh):** Specialized niche
   - Risk: Narrow focus; supply chain dependent
   - Opportunity: Premium fresh offerings, seasonal products

4. **Cluster 4 (Diversified):** Balanced middle segment
   - Risk: Average profitability; easy to lose to competitors
   - Opportunity: Cross-category bundles, loyalty programs

---

## Visualizations Generated

1. **Feature Distributions** — By customer spending
2. **Elbow Curve** — WCSS vs. number of clusters
3. **Silhouette Plot** — Cluster quality assessment
4. **Cluster Centers** — Mean feature values per cluster
5. **Scatter Plots** — Clusters in 2D (PCA reduced)
6. **Box Plots** — Feature distributions per cluster

---

## Agricultural Connection

### How This Applies to Farming:

1. **Farmer Typology:**
   - **Cluster 1 (Commercial Large-Scale):** High-input, high-output, diversified crops
   - **Cluster 2 (Subsistence Small-Holders):** Low input, low output, focus on staples
   - **Cluster 3 (Specialty Crops):** Focus on high-value products (fruits, vegetables)
   - **Cluster 4 (Mixed Farms):** Diversified production, moderate scale

2. **Extension Service Design:**
   - Different farmers need different advice
   - Subsistence farmers: Basic practices, climate adaptation
   - Commercial farmers: Advanced techniques, market information
   - Specialty farmers: Specific crop knowledge, supply chains

3. **Input Distribution:**
   - Subsistence farmers: Need affordable inputs, savings groups
   - Commercial farmers: Volume discounts, credit lines
   - Specialty farmers: Premium inputs, technical support

4. **Market Information:**
   - Subsistence farmers: Local market prices
   - Commercial farmers: Export prices, contracts
   - Specialty farmers: Premium market channels

5. **Climate Adaptation:**
   - Smallholders: Drought-resistant varieties
   - Commercial farmers: Irrigation investment, crop insurance
   - Specialty farmers: Climate-specific high-value crops

6. **Regional Clustering:**
   - Similar agro-ecological zones → Similar farmer needs
   - Group extension activities by regional cluster
   - Tailor recommendations to cluster characteristics

---

## Key Differences: Supervised vs. Unsupervised

### Supervised Learning (Classification)
- **Known outcome:** Predefined labels (e.g., "will churn" or "won't churn")
- **Goal:** Train model to predict labels for new data
- **Evaluation:** Compare predictions to actual labels
- **Example:** Customer Churn Analysis project

### Unsupervised Learning (Clustering)
- **No predefined labels:** Discover natural groupings
- **Goal:** Find hidden patterns and structure
- **Evaluation:** Cluster quality metrics (silhouette, inertia)
- **Example:** This Customer Segmentation project

### When to Use Each:
- **Supervised:** When you have labeled historical data
- **Unsupervised:** When exploring new domains or discovering patterns

---

## Skills Demonstrated

✅ Unsupervised learning fundamentals  
✅ K-Means clustering algorithm  
✅ Determining optimal number of clusters  
✅ Feature scaling for distance-based methods  
✅ Cluster profiling and interpretation  
✅ Multi-dimensional data visualization  
✅ Agricultural segmentation strategy  

---

**Last Updated:** June 2026

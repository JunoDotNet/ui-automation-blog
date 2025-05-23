# Test Plan – Personal Blog UI

## 🎯 Goal
Validate that the personal blog’s core UI elements work as expected, are visually consistent, and handle user interactions without regressions.

## 📋 Scope

### In Scope
- Homepage layout and responsiveness
- Navigation between categories and posts
- Search functionality
- Blog post layout (text, image)
- Basic accessibility (contrast, tab flow)

### Out of Scope
- Admin panel
- API security
- Mobile browser testing (will test on desktop Chrome only for now)

## 🧪 Types of Testing
- Manual exploratory testing
- UI automation using Cypress
- Visual bug identification with Figma
- Basic accessibility testing (checklist + Cypress-Axe if added)

## ✅ Test Environments
- Localhost (`http://localhost:3000`)
- Deployed site (if available)

## 🧰 Tools
- Cypress
- Figma (for visual audits)
- GitHub Actions (CI)

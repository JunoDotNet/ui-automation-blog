# Test Cases – Personal Blog UI

---

### ✅ TC001 – Homepage Loads Correctly

- **Precondition**: User visits the homepage
- **Steps**:
  1. Open browser
  2. Navigate to `http://localhost:3000/blog`
- **Expected Result**: Homepage loads with site title, intro text, and visible category buttons
- **Actual Result**: Category buttons are displayed, but the homepage layout has not been implemented yet

---

### ✅ TC002 – Navigation to Category View

- **Precondition**: Homepage is loaded
- **Steps**:
  1. Click on any category button (e.g., "Tech Tutorials")
- **Expected Result**: Category page loads and displays blog posts under the selected category
- **Actual Result**: Category page loads correctly and displays posts fetched from Contentful

---

### ✅ TC003 – Post Opens from Category View

- **Precondition**: Category page is visible
- **Steps**:
  1. Click on a post title or image
- **Expected Result**: Post view opens showing the full title, publish date, body text, and images
- **Actual Result**: Post displays, but content escapes the UI frame and does not utilize available space effectively

---

### ✅ TC004 – Basic Accessibility Check

- **Precondition**: Homepage is loaded
- **Steps**:
  1. Press the `Tab` key repeatedly
- **Expected Result**: Interactive elements receive a visible focus ring and follow a logical tab order
- **Actual Result**: The "Home" button is functional, and focus behavior appears correct

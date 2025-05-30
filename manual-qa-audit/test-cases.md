# Manual Test Cases – Blog QA

## Test Case 1 – Open Resume Window
**Steps**  
1. Click Resume icon on desktop  
2. Observe if the window expands properly

**Expected:** PDF displays full height  
**Actual:** PDF appears constrained (bug)  
**Status:** ❌ Fail

---

## Test Case 2 – Navigate Blog Category
**Steps**  
1. Click Blog icon  
2. Choose a category  
3. Verify post list loads

**Expected:** Posts appear related to category  
**Actual:** Posts load correctly  
**Status:** ✅ Pass

---

## Test Case 3 - Open Blog Post
**Steps**
1. Click Blog icon
2. Choose a category
3. Click a post title 

**Expected:** Post view opens with full content, image, and publish date
**Actual:** Post view loads correctly with expected data 
**Status:** ✅ Pass

---

## Test Case 4 - Return to Homepage
**Steps**
1. Click Blog icon
2. Navigate to a post
3. Click "Home" button  

**Expected:** Homepage loads without full page refresh
**Actual:** Homepage loads properly with XP-style interface
**Status:** ✅ Pass 

---

## Test Case 5 - Contact Window Behavior 
**Steps**
1. Click the contact icon
2. Verify that the window appears
3. Try dragging or closing the window  

**Expected:** Window appears on top layer and responds to drag/close
**Actual:** Window opens and behaves correctly
**Status:** ✅ Pass

---

## Test Case 6 - Category with No Posts
**Steps**
1. Click Blog icon
2. Select a category that has no posts 

**Expected:** “No posts in this category yet.” message displayed
**Actual:** UI appears blank or glitchy with no feedback
**Status:** ❌ Fail

---

## Test Case 7 – Search Miss Behavior
**Steps**
1. Click Search
2. Enter gibberish (e.g., "zzzzzz") into search bar

**Expected:** Friendly “No results found.” message shown
**Actual:** Layout shifts or missing feedback
**Status:** ❌ Fail

---

## Test Case 8 – Smooth Slide Transition
**Steps**

1. Click Blog icon
2. Select any category with posts
3. Click a post to view it
4. Use “Back” to return to category view
5. Click “Home”

**Expected:** Each transition animates smoothly in the correct direction, with no flash or page reload
**Actual:** All slides animate as expected with retained state and visuals
**Status:** ✅ Pass
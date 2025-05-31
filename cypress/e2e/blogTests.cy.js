describe('Blog QA Test', () => {
  it('Visits the homepage', () => {
    cy.visit('https://jonwithablog.com');

    cy.contains('Blog', { timeout: 6000 }) // Wait for up to 6 seconds
      .should('be.visible')                // Confirm it's actually visible
      .click({ force: true });             // Click even if it's mid-animation
    
    cy.contains('Video Updates', { timeout: 6000 }).should('exist');
    cy.contains('Video Updates').click();
    
    cy.get('img[alt*="Blog Post"]', { timeout: 6000 }).should('be.visible');

    // Click the first post image
    cy.get('img[alt*="Blog Post"]').first().click();

    // Check for post content
    cy.get('h1').should('exist');         // Post title
    cy.get('img').should('be.visible');   // Post image (in full view)


    cy.contains('Quit').click();
    cy.contains('Welcome').should('exist');
  });
});

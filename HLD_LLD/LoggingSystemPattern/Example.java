// Chain of responsibility Design pattern

// Usage 
// 1. ATM
// 2. Vendingg Machine 
// 3. Logger

// when a Client send a request then it 
// goes to a series of receiver object now whichever
// first processes it will send the response else it will propogate

// For ATM
// when we request for 2600 rs then it first goes to 2000 handler if its able to fulfill that it will return else it will go to 500 handler if its able to proceed it gived else goes to next 100 rs handler


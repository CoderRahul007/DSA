'''
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32 



add | --- product ---|--givenNumbers --| --- product (store 0) ---
 3  |      [3]       |     [3]         |         [3]
 0  |     [3,0]      |    [3, 0]       |        [3,0]
 5  |      [5]       |   [3, 0, 5]     |       [3, 0, 0]  !lose info
 2  |     [5,10]     |  [3, 0, 5, 2]   |     [3, 0, 0, 0] !lose infok = 1 < product.size(): then as normal, return product.get(product.size()-1) / product.get(product.size() - k - 1) = 10 / 5 = 2.
k = 2 = product.size(): return product.get(product.size() - k - 1). Because all of the previous entries would be 0, then just return the last entry (product of all non-zero entries after the last zero entry)
k = 3 > product.size(): return 0. product only stores the product of non-zero entries after the last zero seen.
'''
class ProductOfNumbers:

    def __init__(self):
        self.prod=[]
    def add(self, num: int) -> None:
        if num ==0:
            self.prod=[]
        elif self.prod:
            self.prod.append(self.prod[-1]*num)    
        else:
            self.prod.append(num)        
    def getProduct(self, k: int) -> int:
        if k>len(self.prod):
            return 0
        elif k==len(self.prod):
            return self.prod[-1]        
        return self.prod[-1]// self.prod[-k-1]
      
        
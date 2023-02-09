def mergeArrays(a,b,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        res = []       
        
        i = 0
        j = 0
        
        prev = None
     
        while i < n and j < m:
            if a[i] < b[j]:
                if a[i] != prev:
                    res.append(a[i])
                    prev = a[i]
                i += 1
            elif a[i] > b[j]:
                if b[j] != prev:
                    res.append(b[j])
                    prev = b[j]
                j += 1
            else:
                if a[i] != prev:
                    res.append(a[i])
                    prev = a[i]
                i += 1
                j += 1
                 
        while i < n:
            if a[i] != prev:
                res.append(a[i])
                prev = a[i]
            i += 1
     
        while j < m:
            if b[j] != prev:
                res.append(b[j])
                prev = b[j]
            j += 1
        
        return res
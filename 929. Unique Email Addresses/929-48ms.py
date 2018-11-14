class Solution
    def numUniqueEmails(self, emails)
        
        type emails List[str]
        rtype int
        
        final = []
        k = []
        
        for i in emails
            x = i[1i.find(@)].replace(.,)    #剔除.
            y = x[1x.find(+)]+i[i.find(@)len(i)]
            if y not in k
                k.append(y)        
            
        return len(k)
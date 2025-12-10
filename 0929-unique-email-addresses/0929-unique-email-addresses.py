class Solution(object):
    def numUniqueEmails(self, emails):
        seen = set()
        
        for email in emails:
            local, domain = email.split("@")
            
            #ignore everything after '+'
            if '+' in local:
                local = local[:local.find('+')]
            
            #remove all dots
            local = local.replace(".", "")
            
            cleaned = local + "@" + domain
            seen.add(cleaned)
        
        return len(seen)

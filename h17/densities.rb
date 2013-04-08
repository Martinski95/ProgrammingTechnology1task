class Array
    def densities
        hash = self.occurences_count
        tempArray = []
        self.each_index do |x|
            tempArray[x] = hash[self[x]]
        end
        tempArray
    end
end
class Array
    def to_hash
        hash = {}
        self.each do |arr|
            if arr.kind_of?(Array)
                hash[arr[0]] = arr[1]
            else
                break
            end
        end
        hash
    end
end
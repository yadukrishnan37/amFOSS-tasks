

def prime(num)
    count = 0
    for i in 1..num
        if num % i == 0
            count += 1
        end
    end
    return count
end

puts "Enter the limit: "
n = gets.chomp.to_i
puts n

for i in 2..n+1
    if prime(i) == 2
        puts i
    end
end


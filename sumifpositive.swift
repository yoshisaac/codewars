//https://www.codewars.com/kata/5715eaedb436cf5606000381/train/swift

func sumOfPositives (_ numbers: [Int] ) -> Int {
    var sum: Int = 0
    for num in numbers {
        if num > 0 {
            sum += num
        }
    }
    return sum
}

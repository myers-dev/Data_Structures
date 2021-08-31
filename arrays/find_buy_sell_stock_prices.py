def find_buy_sell_stock_prices(array):
  # walking over the array and keeping track of the following
  # minimum, current value , current profit , max profit

  #print (array)
  minimum = 0
  profit = [0, 1, array[1] - array[minimum]]

  for index in range(2,len(array)):
    if array[index - 1] < array[minimum]:
        minimum = index - 1
    #print(f"for {index} minimum located on position {minimum} and equal to {array[minimum]}")

    if array[index] - array[minimum] > profit[2]:   
        #print(f"we are going to change profit because {array[index] - array[minimum]} is more than {profit[2]} ")
        profit = [ minimum, index , array[index] - array[minimum]] 
        
    

  #print(profit[2])
  return ([array[profit[0]],array[profit[1]]])

a=[1,2,3,4,5,6,7,8]  
print(find_buy_sell_stock_prices(a))



# https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
# https://www.askthecode.com/post/stock-buy-and-sell-problem-using-kadane-s-algorithm-askthecode
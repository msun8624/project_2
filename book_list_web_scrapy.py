# read data from file and convert to proper format
book_list = pd.read_csv('books.csv', encoding='utf-8',thousands=',')

# replace na values
book_list.year.fillna(value=9999, inplace=True)
book_list.pages.fillna(value=9999, inplace=True)
book_list.ISBN.fillna(value='9'*13, inplace=True)

# drop columns with too many NA
book_list.drop(['voted','num_ratings'], axis=1, inplace=True)

# convert data to proper type
book_list.year = book_list.year.astype('int')
book_list.pages = book_list.pages.astype('int')
book_list.ISBN = book_list.ISBN.astype('int')

# sort the books according to ranking
book_list.sort_values('ranking', inplace=True)

# write to file for presentation in R
book_list.to_csv('book_list.csv', index=False)

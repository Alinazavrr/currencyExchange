const {useState, useEffect} = React;

function App() {
  const [selectedCurrency, setSelectedCurrency] = useState('USD');

  const handleCurrencyChange = (event) => {
    setSelectedCurrency(event.target.value);
  };

  const getRates = () => {
    // Формирование URL с параметром
    const url = `http://localhost:8000/api/currency-rates/?name=${selectedCurrency}`;

    // Выполнение GET-запроса
    fetch(url)
      .then(response => response.json())
      .then(data => {
        // Обработка данных
        console.log(data);
      })
      .catch(error => {
        console.error('Ошибка при выполнении GET-запроса:', error);
      });
  };

  return (
    <div>
      <select id="currency-dropdown" value={selectedCurrency} onChange={handleCurrencyChange}>
        <option value="USD">USD</option>
        <option value="EUR">EUR</option>
        <option value="GBP">GBP</option>
        {/* Другие валюты */}
      </select>

      {/* Кнопка, при нажатии которой будет вызвана функция getRates() */}
      <button onClick={getRates}>Получить курсы валют</button>
    </div>
  );
}

var elem = document.getElementById('get-rates-app');
ReactDOM.render(<App />, elem);


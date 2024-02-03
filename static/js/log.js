const {useState, useEffect} = React; // импорт хуков
import ReactDOM from 'react-dom';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    try {
      // Ваш код для отправки запроса на сервер и обработки ответа с токеном
      // Пример:
       const response = await fetch('http://yourdomain.com/api/token/', {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json',
           },
           body: JSON.stringify({
               username,
               password,
           }),
       });

       const data = await response.json();

       if (data.access) {
           localStorage.setItem('token', data.access);
           console.log('Login successful');
       } else {
           console.log('Invalid credentials');
       }

      console.log('Login successful'); // Удалите эту строку, когда будете использовать настоящий код обработки входа
    } catch (error) {
      console.error('Error during login:', error);
    }
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <div className="form-group">
        <label htmlFor="username">Username</label>
        <input type="text" id="username" placeholder="Enter your username" value={username} onChange={(e) => setUsername(e.target.value)} />
      </div>
      <div className="form-group">
        <label htmlFor="password">Password</label>
        <input type="password" id="password" placeholder="Enter your password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </div>
      <div className="form-group">
        <button onClick={handleLogin}>Login</button>
      </div>
    </div>
  );
}

ReactDOM.render(<Login />, document.getElementById('loginApp'));
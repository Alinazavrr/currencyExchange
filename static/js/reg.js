const {useState, useEffect} = React;
import ReactDOM from 'react-dom';

function Registration() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleRegistration = async () => {
    try {
      // Ваш код для отправки запроса на сервер и обработки ответа о успешной регистрации
      // Пример:
       const response = await fetch('http://yourdomain.com/api/register/', {
           method: 'POST',
           headers: {
               'Content-Type': 'application/json',
           },
           body: JSON.stringify({
               username,
               email,
               password,
           }),
       });

       const data = await response.json();

       if (data.id) {
           console.log('Registration successful');
           // Перенаправление на другую страницу после успешной регистрации
           // window.location.href = '/success'; // Замените '/success' на путь к вашей целевой странице
       } else {
           console.log('Registration failed');
       }

      console.log('Registration successful'); // Удалите эту строку, когда будете использовать настоящий код обработки регистрации
    } catch (error) {
      console.error('Error during registration:', error);
    }
  };

  return (
    <div className="registration-container">
      <h2>Registration</h2>
      <div className="form-group">
        <label htmlFor="username">Username</label>
        <input type="text" id="username" placeholder="Enter your username" value={username} onChange={(e) => setUsername(e.target.value)} />
      </div>
      <div className="form-group">
        <label htmlFor="email">Email</label>
        <input type="email" id="email" placeholder="Enter your email" value={email} onChange={(e) => setEmail(e.target.value)} />
      </div>
      <div className="form-group">
        <label htmlFor="password">Password</label>
        <input type="password" id="password" placeholder="Enter your password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </div>
      <div className="form-group">
        <button onClick={handleRegistration}>Register</button>
      </div>
    </div>
  );
}

ReactDOM.render(<Registration />, document.getElementById('registrationApp'));
<html>
<head>
  <link rel="stylesheet" href="/static/style.css" />
</head>
<body>
  <table>
    <thead>
      <tr>
        % for key in columns:
          <th>{{key}}</th>
        % end
    </thead>
    <tbody>
    % for doc in docs:
      <tr>
        % for key in columns:
          <td>{{ str(doc[key]) }}</td>
        % end
      </tr>
    % end
    </tbody>
  </table>
</body>
</html>

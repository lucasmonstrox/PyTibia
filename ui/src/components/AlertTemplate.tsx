import { Alert } from '@mui/material';

// TODO: fix params types
const AlertTemplate = ({ message, close, style, options }: any) => (
  <Alert severity={options.type} style={style} onClose={close}>
    {message}
  </Alert>
);

export default AlertTemplate;

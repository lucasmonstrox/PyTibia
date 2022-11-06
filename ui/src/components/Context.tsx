import { createContext, useEffect, useState } from 'react';

export const Context = createContext({} as any);

export const ContextProvider = ({ children }: any) => {
  const [context, setContext] = useState();
  useEffect(() => {
    async function initContext() {
      try {
        // @ts-ignore
        const res = await window.api.getContext();
        setContext(res);
      } catch (err) {
        console.log(`🚀 ~ err`, err);
      }
    }
    initContext();
  }, []);
  return (
    <Context.Provider value={{ context, setContext }}>
      {context ? children : null}
    </Context.Provider>
  );
};

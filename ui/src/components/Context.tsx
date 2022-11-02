import { createContext, useState } from 'react';
import { HealthPotions } from '../types/health.types';
import { ManaPotions } from '../types/mana.types';

export const Context = createContext({} as any);

export const ContextProvider = ({ children }: any) => {
  const [healthPotion, setHealthPotion] = useState<HealthPotions>(
    HealthPotions.HealthPotion
  );
  const [quantityOfHealthPotionsToRefill, setQuantityOfHealthPotionsToRefill] =
    useState<number>(10);
  const [manaPotion, setManaPotion] = useState<ManaPotions>(
    ManaPotions.ManaPotion
  );
  const [quantityOfManaPotionsToRefill, setQuantityOfManaPotionsToRefill] =
    useState<number>(10);
  return (
    <Context.Provider
      value={{
        refill: {
          health: {
            item: healthPotion,
            quantity: quantityOfHealthPotionsToRefill,
          },
          mana: {
            item: manaPotion,
            quantity: quantityOfManaPotionsToRefill,
          },
        },
        setHealthPotion,
        setQuantityOfHealthPotionsToRefill,
        setManaPotion,
        setQuantityOfManaPotionsToRefill,
      }}
    >
      {children}
    </Context.Provider>
  );
};

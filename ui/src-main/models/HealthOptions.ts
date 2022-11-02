import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

@Entity()
export default class HealthOptions {
  @PrimaryGeneratedColumn()
  id!: number;

  @Column()
  potion!: number;

  @Column()
  enabled!: boolean;

  @Column()
  hotkey?: string;
}

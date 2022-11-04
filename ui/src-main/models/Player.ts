import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

@Entity()
export class Player {
  @PrimaryGeneratedColumn()
  id!: string;

  @Column({ unique: true })
  nick!: string;
}

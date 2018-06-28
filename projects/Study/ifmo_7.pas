var
  cur, max_val, max_dis:integer;
  n,i, counter:byte;
begin
  assign(input, 'input.txt');
  assign(output, 'output.txt');
  reset(input);
  rewrite(output);
  max_val:= 0;
  max_dis:= 1;
  counter:= 1;
  readln(n);
  for i:=1 to n do
    begin
      read(cur);
      if cur > max_val then
        begin
          if counter <> 1 then max_dis:= max(max_dis, counter);
          max_val:= cur;
          counter:= 1;
        end
      else
        inc(counter);
    end;
  write(max_dis);
  close(input);
  close(output);
end.
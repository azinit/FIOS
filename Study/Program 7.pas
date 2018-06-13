var
  n,s,q,k,i,c:integer;
  a:array [1..100] of integer;
begin
  assign(input, 'input.txt');
  assign(output, 'output.txt');
  reset(input);
  rewrite(output);
  readln(n);
  q:=maxint;
  s:=1;
  c:=1;
  for i:=1 to n do
    read(a[i]);
  for i:=1 to n do
    begin
      k:= a[i];
      if k < q then
        begin
          if c <> 1 
            then 
              s:= max(s, c);
          q:= k;
          c:= 1;
        end
      else
        inc(c);
    end;
  write(s);
  close(input);
  close(output);
end.